# Standard Library
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
from transliterate import translit

# My Stuff
from credentials import (
    REDIS_DB,
    REDIS_HOST,
    REDIS_PORT,
)
from db.connection import db_engine
from db.models import (
    Athlete,
    Race,
    ReplaceName,
)
from rating_bot import races as races_module
from rating_bot.bot_instance import (
    bot,
    user_is_admin,
)
from rating_bot.race_file_parse import (
    merge_athletes,
    parse_csv,
)
from rating_bot.results import (
    athlete_report,
    season_report,
)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s:%(message)s",
)
TEMP_PATH = os.path.join(os.path.dirname(__file__), "data")
redis_connection = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True,
    encoding="utf-8",
)


@bot.message_handler(
    commands=["my_id", "myid"],
    chat_types=["private"],
)
def command_my_id(message: Message):
    """ """
    bot.reply_to(message, str(message.from_user.id))


@bot.message_handler(
    commands=["help"],
    chat_types=["private"],
    func=user_is_admin,
)
def command_help(message: Message):
    text = """
Формат файла CSV:

Имя | Номер на гонке | Время | Пол (m - мужской, f - женский)

Пример:
Горбачев Иван | 75 | 0:27:05.5 | m

Raw csv data:
```csv
Горбачев Иван;75;0:27:05.5;m
Канафин Байжан;54;0:27:48.5;m
Крупяков Геннадий;67;0:28:06.8;m
Иргалиев Ильяс;46;0:28:24.4;m
Сладков Евгений;68;0:29:05.5;m
Морозов Алексей;93;0:29:26.3;m
Алмагамбетов Рустам;124;0:29:32.4;m
Ветров Владимир;10;0:29:56.6;m
Андреев Иван;22;0:30:00.8;m
Юдкин Вадим;94;0:30:19.5;m
Антонюк Артем;82;0:30:24.2;m
Хадылбек Кайрат;25;0:30:33.3;m
Сорокин Глеб;101;0:30:46.1;m
Таргынов Аян;15;0:31:02.3;m
```
"""
    bot.reply_to(message, text, parse_mode="Markdown")


@bot.message_handler(
    commands=["rating"],
    chat_types=["private"],
    func=user_is_admin,
)
def rating(message: Message):
    filename = season_report()
    with open(filename, "r") as csvfile:
        bot.send_document(
            chat_id=message.chat.id,
            document=csvfile,
        )


@bot.message_handler(
    commands=["athlete_report"],
    chat_types=["private"],
    func=user_is_admin,
)
def athlete_report_command(message: Message):
    msg = bot.reply_to(message, "Введите имя атлета")
    bot.register_next_step_handler(
        msg,
        report_athlete_name_inputed,
    )


def report_athlete_name_inputed(message):
    athlete_name = message.text
    with Session(db_engine) as session:
        athlete = session.scalars(
            select(Athlete).where(Athlete.name == athlete_name)
        ).first()
        if not athlete:
            bot.reply_to(message, "Атлет не найден")
            return
        filename = athlete_report(athlete.id)
        with open(filename, "r") as csvfile:
            bot.send_document(
                chat_id=message.chat.id,
                document=csvfile,
            )


def download_file(file_id: str) -> str:
    """
    Returns path to downloaded file
    """
    try:
        if not os.path.exists(TEMP_PATH):
            os.mkdir(TEMP_PATH)
    except FileExistsError as e:
        logging.error(e, exc_info=True)
    except Exception as e:
        logging.error(e, exc_info=True)
        raise e
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = file_info.file_path.split("/")[-1]
    src = os.path.join(TEMP_PATH, file_name)
    with open(src, "wb") as new_file:
        new_file.write(downloaded_file)
    return src


@bot.message_handler(content_types=["document"])
def handle_csv(message):
    file_ext = message.document.file_name.split(".")[-1].lower()

    if file_ext == "csv":
        keyboard = InlineKeyboardMarkup()
        with Session(db_engine) as session:
            races = session.scalars(select(Race).order_by(Race.date_start.desc())).all()
            redis_connection.set(
                f"file_id#{message.from_user.id}", message.document.file_id
            )
            for race in races:
                button = InlineKeyboardButton(
                    text=race.name,
                    callback_data=f"file_race${race.id}",
                )
                logging.debug(button)
                keyboard.add(button)
        new_race_button = InlineKeyboardButton(
            text="Новая гонка",
            callback_data="new_race",
        )
        keyboard.add(new_race_button)
        bot.reply_to(
            message,
            "Выберите гонку для которой загружается файл",
            reply_markup=keyboard,
        )

    else:
        bot.reply_to(message, "Мне нужен файл с расширением .csv")


@bot.callback_query_handler(func=lambda c: c.data.startswith("file_race$"))
def handle_file_race(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    bot.delete_message(
        chat_id=chat_id,
        message_id=callback_query.message.message_id,
    )
    race_id = int(callback_query.data.split("$")[1])
    file_id = str(redis_connection.get(f"file_id#{callback_query.from_user.id}"))
    file = download_file(file_id)
    count = parse_csv(file, race_id)
    bot.send_message(
        chat_id=chat_id,
        text=f"Файл загружен {count=}",
    )


@bot.message_handler(
    commands=["merge"],
    chat_types=["private"],
    func=user_is_admin,
)
def merge(message: Message):
    """ """
    bot.reply_to(message, "Введите имя атлета 1")
    bot.register_next_step_handler(
        message,
        merge_athlete_1,
    )


def merge_athlete_1(message: Message):
    chat_id = message.chat.id
    assert message.text
    redis_connection.set(f"merge_athlete_1#{chat_id}", message.text)
    bot.reply_to(message, "Введите имя атлета 2")
    bot.register_next_step_handler(
        message,
        merge_athlete_2,
    )


def merge_athlete_2(message: Message):
    chat_id = message.chat.id
    athlete_1_name = redis_connection.get(f"merge_athlete_1#{chat_id}")
    athlete_2_name = message.text
    with Session(db_engine) as session:
        athlete_1 = session.scalar(
            select(Athlete).where(Athlete.name == athlete_1_name)
        )
        if not athlete_1:
            bot.reply_to(message, "Атлет 1 не найден")
            return
        athlete_2 = session.scalar(
            select(Athlete).where(Athlete.name == athlete_2_name)
        )
        if not athlete_2:
            bot.reply_to(message, "Атлет 2 не найден")
            return
        merge_athletes(athlete_1.id, athlete_2.id)
        try:
            replace_name = ReplaceName(
                name=athlete_2.name,
                replace_name=athlete_1.name,
            )
            session.add(replace_name)
            session.commit()
        except Exception as e:
            logging.error(e, exc_info=True)
            return
        bot.reply_to(message, f"Атлеты объединены остался только {athlete_1_name}")


@bot.message_handler(
    commands=["translit"],
    chat_types=["private"],
    func=user_is_admin,
)
def translit_command(message: Message):
    """ """
    with Session(db_engine) as session:
        athletes = session.scalars(select(Athlete)).all()
        for athlete in athletes:
            translit_name = translit(athlete.name, "ru", reversed=False)
            if translit_name == athlete.name:
                continue
            original_athlete = session.scalar(
                select(Athlete).where(Athlete.name == translit_name)
            )
            if original_athlete:
                merge_athletes(original_athlete.id, athlete.id)
                continue
            redis_connection.set(f"translit#{athlete.id}", translit_name)
            keyboard = InlineKeyboardMarkup()
            yes_button = InlineKeyboardButton(
                text="Да",
                callback_data=f"translit_yes${athlete.id}",
            )
            no_button = InlineKeyboardButton(
                text="Нет",
                callback_data=f"translit_no${athlete.id}",
            )
            keyboard.add(yes_button, no_button)

            bot.send_message(
                chat_id=message.chat.id,
                text=f"Делаем транслит {athlete.name} -> {translit_name}",
                reply_markup=keyboard,
            )


@bot.callback_query_handler(func=lambda c: c.data.startswith("translit_yes$"))
def translit_yes(callback_query: CallbackQuery):
    bot.delete_message(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
    )
    athlete_id = int(callback_query.data.split("$")[1])
    translit_name = str(redis_connection.get(f"translit#{athlete_id}"))
    with Session(db_engine) as session:
        athlete = session.get(Athlete, athlete_id)
        assert athlete
        athlete.name = translit_name
        session.commit()
    bot.reply_to(callback_query.message, "Транслит сделан")


@bot.callback_query_handler(func=lambda c: c.data.startswith("translit_no$"))
def translit_no(callback_query: CallbackQuery):
    bot.delete_message(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
    )


if __name__ == "__main__":
    bot.infinity_polling()
