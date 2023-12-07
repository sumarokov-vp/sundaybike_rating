# Standard Library
import csv
import logging
import os
from datetime import datetime

# Third Party Stuff
import redis
from sqlalchemy import select
from sqlalchemy.orm import Session
from telebot.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

# My Stuff
from credentials import (
    REDIS_DB,
    REDIS_HOST,
    REDIS_PORT,
)
from db.connection import db_engine
from db.models import (
    Athlete,
    Category,
    CategoryResult,
    Race,
    RaceClass,
    RaceResult,
    Sex,
)
from rating_bot.bot_instance import bot
from rating_bot.results import (
    places_rating,
    race_report,
)

redis_connection = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True,
    encoding="utf-8",
)
TEMP_PATH = os.path.join(os.path.dirname(__file__), "data")


@bot.message_handler(
    commands=["races"],
    chat_types=["private"],
)
def command_races(message: Message):
    """ """
    with Session(db_engine) as session:
        races = session.scalars(select(Race).order_by(Race.date_start.desc())).all()
        # if not races:
        #     bot.reply_to(message, "Нет ни одной гонки")
        keyboard = InlineKeyboardMarkup()
        for race in races:
            button = InlineKeyboardButton(
                text=f"{race.date_start:%d-%m-%Y} - {race.name}",
                callback_data=f"race${race.id}",
            )
            keyboard.add(button)
        new_race_button = InlineKeyboardButton(
            text="Новая гонка", callback_data="new_race"
        )
        keyboard.add(new_race_button)
        bot.reply_to(message, "Выберите гонку", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith("race$"))
def race_selected(callback_query: CallbackQuery):
    race_id = int(callback_query.data.split("$")[1])
    places_rating(race_id)
    filename = race_report(race_id=race_id)
    with open(filename, "r") as csvfile:
        bot.send_document(
            chat_id=callback_query.message.chat.id,
            document=csvfile,
        )


@bot.callback_query_handler(func=lambda call: call.data.startswith("new_race"))
def new_race(callback_query: CallbackQuery):
    message = bot.send_message(
        chat_id=callback_query.message.chat.id,
        text="Введите название гонки",
    )
    bot.register_next_step_handler(
        message,
        new_race_name,
    )


def new_race_name(message: Message):
    chat_id = message.chat.id
    if not message.text:
        bot.reply_to(message, "Название не может быть пустым")
        return
    redis_connection.set(f"new_race_name#{chat_id}", message.text)
    message = bot.send_message(
        chat_id=chat_id,
        text="Введите дату начала гонки в формате ДД.ММ.ГГГГ",
    )
    bot.register_next_step_handler(
        message,
        new_race_date,
    )


def new_race_date(message: Message):
    chat_id = message.chat.id
    if not message.text:
        bot.reply_to(message, "Дата не может быть пустой")
        return
    try:
        datetime.strptime(message.text, "%d.%m.%Y")
    except ValueError:
        bot.reply_to(message, "Неверный формат даты")
        return
    redis_connection.set(f"new_race_date#{chat_id}", message.text)
    keyboard = InlineKeyboardMarkup()
    with Session(db_engine) as session:
        classes = session.scalars(select(RaceClass)).all()
        for race_class in classes:
            button = InlineKeyboardButton(
                text=race_class.name,
                callback_data=f"race_class${race_class.id}",
            )
            keyboard.add(button)
    message = bot.send_message(
        chat_id=chat_id,
        text="Введите класс гонки",
        reply_markup=keyboard,
    )


@bot.callback_query_handler(func=lambda c: c.data.startswith("race_class$"))
def new_race_class(callback_query: CallbackQuery):
    class_id = int(callback_query.data.split("$")[1])
    chat_id = callback_query.message.chat.id
    race_date_str = str(redis_connection.get(f"new_race_date#{chat_id}"))
    try:
        race_date = datetime.strptime(race_date_str, "%d.%m.%Y")
    except ValueError as e:
        logging.error(e, exc_info=True)
        return

    race_name = redis_connection.get(f"new_race_name#{chat_id}")
    with Session(db_engine) as session:
        race = Race(
            name=race_name,
            date_start=race_date,
            race_class_id=class_id,
        )
        session.add(race)
        session.commit()
    bot.reply_to(callback_query.message, "Гонка добавлена")


def race_report_old(race_id: int) -> str:
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

            # Absolute results
            csv_writer.writerow(["Абсолют", "", "", "", "", "", "", "", ""])
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

            # Category results
            csv_writer.writerow(["Категории", "", "", "", "", "", "", "", ""])
            categories = session.scalars(select(Category).order_by(Category.name)).all()
            sexes = session.scalars(select(Sex)).all()
            category_results = session.scalars(
                select(CategoryResult)
                .join(CategoryResult.result)
                .where(RaceResult.race_id == race_id)
                .order_by(CategoryResult.place)
            ).all()
            for sex in sexes:
                csv_writer.writerow([f"{sex.name}", "", "", "", "", "", "", "", ""])
                for category in categories:
                    csv_writer.writerow(
                        [f"{category.name}", "", "", "", "", "", "", "", ""]
                    )

                    csv_writer.writerow(
                        [
                            "Место",
                            "ФИО",
                            "Время",
                            "Очки",
                            "",
                            "",
                            "",
                            "",
                            "",
                        ]
                    )
                    for c_result in category_results:
                        if c_result.result.athlete.sex_id != sex.id:
                            continue
                        if c_result.category_id != category.id:
                            continue
                        csv_writer.writerow(
                            [
                                c_result.place,
                                c_result.result.athlete.name,
                                c_result.result.result_time,
                                c_result.points,
                                "",
                                "",
                                "",
                                "",
                                "",
                            ]
                        )

        return filename
