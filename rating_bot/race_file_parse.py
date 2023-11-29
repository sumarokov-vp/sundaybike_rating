# Standard Library
import csv
import logging
from datetime import (
    datetime,
    timedelta,
)

# Third Party Stuff
from sqlalchemy import (
    select,
    update,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

# My Stuff
from db.connection import db_engine
from db.models import (
    Athlete,
    RaceResult,
    ReplaceName,
)


def parse_csv(file, race_id) -> int:
    csv_reader = csv.reader(file, delimiter=";")
    with Session(db_engine, expire_on_commit=False) as session:
        with open(file, "r") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")
            count = 0
            for row in csv_reader:
                logging.debug(f"row: {row}")
                name = row[0]
                name = capitalize_name(name)
                bib_number = row[1]
                time_str = row[2]
                sex = row[3]

                match sex.lower():
                    case "m":
                        sex_id = 1
                    case "f":
                        sex_id = 2
                    case _:
                        sex_id = 3

                race_result = RaceResult(
                    race_id=race_id,
                    athlete_id=get_athlete_by_name(name, sex_id),
                    bib_number=bib_number,
                    result_time=parse_timedelta(time_str),
                )
                try:
                    session.add(race_result)
                    session.commit()
                    count += 1
                except IntegrityError as e:
                    session.rollback()
                    logging.error(e)
    return count


def name_pre_process(name) -> str:
    name = name.replace("ё", "е").replace("Ё", "Е")
    name = name.replace(".", "").replace(",", "")
    name = capitalize_name(name)
    return name


def capitalize_name(name):
    # capitalize all words in name
    words = name.split(" ")
    name = " ".join([word.capitalize() for word in words])
    return name


def get_athlete_by_name(name, sex_id) -> int:
    with Session(db_engine) as session:
        replace_name = session.scalar(
            select(ReplaceName.replace_name).where(ReplaceName.name == name)
        )
        if replace_name:
            name = replace_name
        else:
            replace_name = session.scalar(
                select(ReplaceName.replace_name).where(
                    ReplaceName.name == swap_name(name)
                )
            )
            if replace_name:
                name = replace_name
        athletes = session.scalars(select(Athlete).where(Athlete.name == name)).all()
        athletes_swap = session.scalars(
            select(Athlete).where(Athlete.name == swap_name(name))
        ).all()
        if len(athletes) == 1:
            athlete = athletes[0]
            return athlete.id
        elif len(athletes_swap) == 1:
            athlete = athletes_swap[0]
            return athlete.id
        else:
            prepared_name = capitalize_name(
                name.replace("ё", "е")
                .replace("Ё", "Е")
                .replace(".", "")
                .replace(",", "")
            )
            new_athlete = Athlete(
                name=prepared_name,
                sex_id=sex_id,
            )
            session.add(new_athlete)
            session.commit()
            return new_athlete.id


def swap_name(name) -> str:
    name = name.split(" ")
    try:
        name = name[1] + " " + name[0]
    except IndexError:
        pass

    return name


def merge_athletes(athlete_id1, athlete_id2) -> int:
    with Session(db_engine) as session:
        athlete1 = session.get(Athlete, athlete_id1)
        athlete2 = session.get(Athlete, athlete_id2)
        assert athlete1
        assert athlete2
        session.execute(
            update(RaceResult)
            .where(RaceResult.athlete_id == athlete_id2)
            .values(athlete_id=athlete_id1)
        )
        session.delete(athlete2)
        session.commit()
        return athlete_id1


def parse_timedelta(time_str):
    # Parse the string to a datetime object
    time_str = time_str.replace(" ", "")
    try:
        time_format = "%H:%M:%S.%f"
        # time_format = "%H:%M:%S"
        time_object = datetime.strptime(time_str, time_format)

        # Convert the datetime object to a timedelta object
        time_delta = timedelta(
            hours=time_object.hour,
            minutes=time_object.minute,
            seconds=time_object.second,
            microseconds=time_object.microsecond,
        )
    except ValueError:
        time_format = "%H:%M:%S"
        # time_format = "%H:%M:%S"
        time_object = datetime.strptime(time_str, time_format)

        # Convert the datetime object to a timedelta object
        time_delta = timedelta(
            hours=time_object.hour,
            minutes=time_object.minute,
            seconds=time_object.second,
        )

    return time_delta
