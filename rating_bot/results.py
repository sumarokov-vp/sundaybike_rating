# Standard Library
import csv
import logging
import os
from datetime import datetime
from decimal import Decimal

# Third Party Stuff
import redis
from sqlalchemy import (
    delete,
    func,
    join,
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
    AthleteCategory,
    Category,
    CategoryResult,
    PointsForPlace,
    Race,
    RaceReport,
    RaceResult,
    SeasonReport,
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


def athlete_category(
    session: Session, athlete_id: int, dt: datetime
) -> AthleteCategory | None:
    """Returns AthleteCategory object for athlete_id and date"""
    athlete_category = session.scalars(
        select(AthleteCategory)
        .where(AthleteCategory.athlete_id == athlete_id)
        .where(AthleteCategory.start <= dt)
        .where(AthleteCategory.end >= dt)
        .limit(1)
    ).first()
    return athlete_category


def places_rating(race_id: int):
    """Set race_results.result_place by race_results.result_time"""
    with Session(db_engine) as session:
        # absolute
        sexes = session.scalars(select(Sex)).all()

        categories = session.scalars(select(Category)).all()
        for sex in sexes:
            # Absolute
            results = session.scalars(
                select(RaceResult)
                .join(RaceResult.athlete)
                .where(RaceResult.race_id == race_id)
                .where(Athlete.sex_id == sex.id)
                .order_by(RaceResult.result_time)
            ).all()
            place = 1
            for result in results:
                result.result_place = place
                points = session.scalar(
                    select(PointsForPlace.points)
                    .where(PointsForPlace.place == place)
                    .where(PointsForPlace.sex_id == sex.id)
                )
                if not points:
                    result.result_points = 0
                else:
                    result.result_points = int(
                        Decimal(points) * result.race.race_class.multiplier
                    )
                place += 1

            # Category
            # TODO: можно сделать DB VIEW для этого, тогда можно
            # будет получить категорию атлета сразу в запросе race_results

            logging.debug("Category")
            for category in categories:
                logging.debug(f"Category: {category.name}")
                place = 1
                for result in results:
                    result_athlete_category = athlete_category(
                        session=session,
                        athlete_id=result.athlete_id,
                        dt=result.race.date_start,
                    )
                    if (
                        not result_athlete_category
                        or result_athlete_category.category_id != category.id
                    ):
                        continue
                    session.execute(
                        delete(CategoryResult).where(
                            CategoryResult.result_id == result.id
                        )
                    )
                    points = session.scalar(
                        select(PointsForPlace.points)
                        .where(PointsForPlace.place == place)
                        .where(PointsForPlace.sex_id == sex.id)
                    )
                    if not points:
                        category_points = 0
                    else:
                        category_points = int(
                            Decimal(points) * result.race.race_class.multiplier
                        )
                    CategoryResult(
                        result_id=result.id,
                        category_id=category.id,
                        place=place,
                        points=category_points,
                    )
                    session.add(CategoryResult)
                    place += 1

        session.commit()


def season_report() -> str:
    with Session(db_engine) as session:
        seasons = [2023]
        sexes = session.scalars(
            select(Sex).where(Sex.enabled == True).order_by(Sex.id)
        ).all()
        categories = session.scalars(select(Category).order_by(Category.name)).all()
        filename = "all_time_report.csv"
        filename = os.path.join(TEMP_PATH, filename)
        with open(filename, "w+") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=";")
            for season in seasons:
                logging.debug(f"{season=}")
                for sex in sexes:
                    logging.debug(f"{sex.name=}")
                    for category in categories:
                        logging.debug(f"{category.name=}")
                        csv_writer.writerow(["", "", ""])
                        csv_writer.writerow(
                            [
                                f"Сезон {season} {sex.name} {category.name}",
                                "",
                                "",
                            ]
                        )
                        csv_writer.writerow(["Место", "ФИО", "Очки"])
                        report_data = session.scalars(
                            select(SeasonReport)
                            .where(SeasonReport.season == season)
                            .where(SeasonReport.sex_id == sex.id)
                            .where(SeasonReport.category_id == category.id)
                            .order_by(SeasonReport.rank)
                        ).all()
                        for report_row in report_data:
                            csv_writer.writerow(
                                [
                                    report_row.rank,
                                    report_row.athlete.name,
                                    report_row.points,
                                ]
                            )
        logging.debug(f"Report finished: {filename}")
        return filename


def athlete_report(athlete_id: int) -> str:
    with Session(db_engine) as session:
        athlete = session.scalar(select(Athlete).where(Athlete.id == athlete_id))
        assert athlete
        athlete_name = athlete.name.replace(" ", "_")
        filename = f"{athlete_name}_report.csv"
        filename = os.path.join(TEMP_PATH, filename)
        with open(filename, "w+") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=";")
            report_data = session.scalars(
                select(RaceReport)
                .join(RaceReport.race)
                .where(RaceReport.athlete_id == athlete_id)
                .order_by(Race.date_start.desc())
            ).all()
            csv_writer.writerow([f"Отчёт по атлету {athlete.name}"] + [""] * 5)
            csv_writer.writerow(
                [
                    "Дата",
                    "Класс гонки",
                    "Гонка",
                    "Категория",
                    "Позиция",
                    "Очки",
                ]
            )
            for report_row in report_data:
                race = report_row.race
                csv_writer.writerow(
                    [
                        race.date_start,
                        race.race_class.name,
                        race.name,
                        report_row.category.name,
                        report_row.rank,
                        report_row.points,
                    ]
                )
    return filename


def season_report_old(year: str) -> str:
    year_begin_date = datetime.strptime(f"{year}-01-01", "%Y-%m-%d")
    year_end_date = datetime.strptime(f"{year}-12-31", "%Y-%m-%d")
    with Session(db_engine) as session:
        races = session.scalars(select(Race)).all()
        for race in races:
            places_rating(race.id)
        stmt = (
            select(
                Athlete.name,
                func.sum(RaceResult.result_points).label("points"),
            )
            .join(RaceResult.athlete)
            .join(RaceResult.race)
            .where(Athlete.sex_id == 1)
            .where(Race.date_start >= year_begin_date)
            .where(Race.date_start <= year_end_date)
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
            .join(RaceResult.race)
            .where(Athlete.sex_id == 2)
            .where(Race.date_start >= year_begin_date)
            .where(Race.date_start <= year_end_date)
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


def season_category_report(year: str) -> str:
    year_begin_date = datetime.strptime(f"{year}-01-01", "%Y-%m-%d")
    year_end_date = datetime.strptime(f"{year}-12-31", "%Y-%m-%d")
    filename = f"categories_season_{year}.csv"
    filename = os.path.join(TEMP_PATH, filename)
    with Session(db_engine) as session:
        races = session.scalars(select(Race)).all()
        for race in races:
            places_rating(race.id)
        sexes = session.scalars(select(Sex)).all()
        categories = session.scalars(select(Category)).all()
        for sex in sexes:
            for category in categories:
                results = session.scalars(
                    select(CategoryResult)
                    .join(CategoryResult.result)
                    .join(RaceResult.athlete)
                    .join(RaceResult.race)
                    .where(CategoryResult.category_id == category.id)
                    .where(Athlete.sex_id == sex.id)
                    .where(Race.date_start >= year_begin_date)
                    .where(Race.date_start <= year_end_date)
                ).all()

    return filename


def race_report(race_id: int) -> str:
    with Session(db_engine) as session:
        race = session.get(Race, race_id)
        assert race
        race_name = (
            race.name.replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
            .replace(":", "_")
        )
        filename = f"{race_name}_report.csv"
        filename = os.path.join(TEMP_PATH, filename)
        with open(filename, "w+") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=";")
            csv_writer.writerow(
                [f"Отчёт по гонке {race.name} ({race.date_start:%d.%m.%Y})"] + [""] * 3
            )
            csv_writer.writerow([f"Класс гонки {race.race_class.name}"] + [""] * 3)
            sexes = session.scalars(
                select(Sex).where(Sex.enabled == True).order_by(Sex.id)
            ).all()
            categories = session.scalars(select(Category).order_by(Category.name)).all()
            for sex in sexes:
                for category in categories:
                    csv_writer.writerow([""] * 4)
                    csv_writer.writerow(
                        [f"{sex.name} категория {category.name}"] + [""] * 3
                    )
                    csv_writer.writerow(
                        [
                            "ФИО",
                            "Позиция",
                            "Время",
                            "Очки",
                        ]
                    )
                    report_data = session.scalars(
                        select(RaceReport)
                        .where(RaceReport.race_id == race_id)
                        .where(RaceReport.sex_id == sex.id)
                        .where(RaceReport.category_id == category.id)
                        .order_by(RaceReport.rank)
                    ).all()
                    for report_row in report_data:
                        csv_writer.writerow(
                            [
                                report_row.athlete.name,
                                report_row.rank,
                                report_row.result_time,
                                report_row.points,
                            ]
                        )
    return filename


if __name__ == "__main__":
    places_rating(1)
