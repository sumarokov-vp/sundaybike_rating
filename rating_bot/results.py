# Standard Library
import csv
import logging
import os
from decimal import Decimal

# Third Party Stuff
from sqlalchemy import (
    func,
    select,
)
from sqlalchemy.orm import Session
from telebot import TeleBot

# My Stuff
from db.connection import db_engine
from db.models import (
    Athlete,
    PointsForPlace,
    Race,
    RaceResult,
    Sex,
)

TEMP_PATH = os.path.join(os.path.dirname(__file__), "data")


def plases_rating(race_id: int):
    """Set race_results.result_place by race_results.result_time"""
    with Session(db_engine) as session:
        results = session.scalars(
            select(RaceResult)
            .where(RaceResult.race_id == race_id)
            .order_by(RaceResult.result_time)
        ).all()
        place = 1
        for result in results:
            result.result_place = place
            points = session.scalar(
                select(PointsForPlace.points).where(PointsForPlace.place == place)
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
        results = session.scalars(
            select(RaceResult)
            .join(RaceResult.athlete)
            .where(RaceResult.race_id == race_id)
            .order_by(Athlete.sex_id)
            .order_by(RaceResult.result_place)
        ).all()
        logging.debug(results)
        filename = race.name.replace(" ", "_") + ".csv"
        filename = os.path.join(TEMP_PATH, filename)
        with open(filename, "w+") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=";")
            csv_writer.writerow(["Место", "ФИО", "Время", "Очки", "Пол"])
            for result in results:
                csv_writer.writerow(
                    [
                        result.result_place,
                        result.athlete.name,
                        result.result_time,
                        result.result_points,
                        result.athlete.sex.name,
                    ]
                )
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
                Sex.name,
            )
            .join(RaceResult.athlete)
            .join(Athlete.sex)
            .group_by(Athlete.name)
            .group_by(Sex.name)
            .group_by(Athlete.sex_id)
            .order_by(Athlete.sex_id)
            .order_by(func.sum(RaceResult.result_points).desc())
        )
        logging.debug(stmt)
        results = session.execute(stmt).all()
        logging.debug(results)
        filename = "all_time_report.csv"
        filename = os.path.join(TEMP_PATH, filename)
        with open(filename, "w+") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=";")
            csv_writer.writerow(["Место", "ФИО", "Очки", "Пол"])
            position = 1
            for result in results:
                if result[1] != "0":
                    csv_writer.writerow(
                        [
                            str(position),
                            result[0],
                            result[1],
                            result[2],
                        ]
                    )
                position += 1
        return filename


if __name__ == "__main__":
    plases_rating(1)
