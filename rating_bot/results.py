# Standard Library
import csv
import logging
import os
from decimal import Decimal

# Third Party Stuff
import redis
from sqlalchemy import (
    func,
    select,
)
from sqlalchemy.orm import Session
from telebot import TeleBot

# My Stuff
from credentials import (
    REDIS_DB,
    REDIS_HOST,
    REDIS_PORT,
)
from db.connection import db_engine
from db.models import (
    Athlete,
    PointsForPlace,
    Race,
    RaceResult,
    Sex,
)

TEMP_PATH = os.path.join(os.path.dirname(__file__), "data")

redis_connection = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True,
    encoding="utf-8",
)


def plases_rating(race_id: int):
    """Set race_results.result_place by race_results.result_time"""
    with Session(db_engine) as session:
        # MEN
        results = session.scalars(
            select(RaceResult)
            .join(RaceResult.athlete)
            .where(RaceResult.race_id == race_id)
            .where(Athlete.sex_id == 1)
            .order_by(RaceResult.result_time)
        ).all()
        place = 1
        for result in results:
            result.result_place = place
            points = session.scalar(
                select(PointsForPlace.points)
                .where(PointsForPlace.place == place)
                .where(PointsForPlace.sex_id == 1)
            )
            if not points:
                result.result_points = 0
            else:
                result.result_points = int(
                    Decimal(points) * result.race.race_class.multiplier
                )
            place += 1

        # WOMEN
        results = session.scalars(
            select(RaceResult)
            .join(RaceResult.athlete)
            .where(RaceResult.race_id == race_id)
            .where(Athlete.sex_id == 2)
            .order_by(RaceResult.result_time)
        ).all()
        place = 1
        for result in results:
            result.result_place = place
            points = session.scalar(
                select(PointsForPlace.points)
                .where(PointsForPlace.place == place)
                .where(PointsForPlace.sex_id == 2)
            )
            if not points:
                result.result_points = 0
            else:
                result.result_points = int(
                    Decimal(points) * result.race.race_class.multiplier
                )
            place += 1
        session.commit()


def race_report(race_id: int) -> str:
    """
    save race results to csv file
    """
    with Session(db_engine) as session:
        race = session.get(Race, race_id)
        assert race
        results_men = session.scalars(
            select(RaceResult)
            .join(RaceResult.athlete)
            .where(RaceResult.race_id == race_id)
            .where(Athlete.sex_id == 1)
            .order_by(RaceResult.result_place)
        ).all()
        logging.debug(results_men)
        filename = race.name.replace(" ", "_") + ".csv"
        filename = os.path.join(TEMP_PATH, filename)
        with open(filename, "w+") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=";")
            csv_writer.writerow(
                ["Место", "ФИО", "Время", "Очки", "", "Место", "ФИО", "Время", "Очки"]
            )
            for result in results_men:
                result_woman = session.scalar(
                    select(RaceResult)
                    .join(RaceResult.athlete)
                    .where(RaceResult.race_id == race_id)
                    .where(RaceResult.result_place == result.result_place)
                    .where(Athlete.sex_id == 2)
                )
                if result_woman:
                    woman_row = [
                        result_woman.result_place,
                        result_woman.athlete.name,
                        result_woman.result_time,
                        result_woman.result_points,
                    ]
                else:
                    woman_row = ["", "", "", ""]
                man_row = [
                    result.result_place,
                    result.athlete.name,
                    result.result_time,
                    result.result_points,
                    "",
                ]
                row = man_row + woman_row
                csv_writer.writerow(row)
        return filename


def all_time_report() -> str:
    with Session(db_engine) as session:
        races = session.scalars(select(Race)).all()
        for race in races:
            plases_rating(race.id)
        stmt = (
            select(
                Athlete.name,
                func.sum(RaceResult.result_points).label("points"),
            )
            .join(RaceResult.athlete)
            .where(Athlete.sex_id == 1)
            .group_by(Athlete.name)
            .group_by(Athlete.sex_id)
            .order_by(func.sum(RaceResult.result_points).desc())
        )
        logging.debug(stmt)
        results_men = session.execute(stmt).all()

        stmt = (
            select(
                Athlete.name,
                func.sum(RaceResult.result_points).label("points"),
            )
            .join(RaceResult.athlete)
            .where(Athlete.sex_id == 2)
            .group_by(Athlete.name)
            .group_by(Athlete.sex_id)
            .order_by(func.sum(RaceResult.result_points).desc())
        )
        results_women = session.execute(stmt).all()
        position = 1
        for result in results_women:
            result_dict = {
                "name": result[0],
                "points": result[1],
            }
            redis_connection.hset(
                f"woman_row#{position}",
                mapping=result_dict,
            )
            position += 1

        womens_max_position = position - 1
        logging.debug(results_men)
        filename = "all_time_report.csv"
        filename = os.path.join(TEMP_PATH, filename)
        with open(filename, "w+") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=";")
            csv_writer.writerow(["Место", "ФИО", "Очки", "", "Место", "ФИО", "Очки"])
            position = 1
            for result in results_men:
                if result[1] != "0":
                    row_man = [str(position), result[0], result[1], ""]

                    if position <= womens_max_position:
                        hget = redis_connection.hgetall(f"woman_row#{position}")
                        if isinstance(hget, dict):
                            woman_result = hget
                        else:
                            raise ValueError("hget is not dict")
                        if woman_result["points"] != "0":
                            row_woman = [
                                str(position),
                                woman_result["name"],
                                woman_result["points"],
                            ]
                        else:
                            row_woman = ["", "", ""]
                    else:
                        row_woman = ["", "", ""]

                    row = row_man + row_woman

                    csv_writer.writerow(row)
                position += 1
        return filename


if __name__ == "__main__":
    plases_rating(1)
