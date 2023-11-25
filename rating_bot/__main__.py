# Standard Library
import logging
import os
from datetime import datetime

# Third Party Stuff
import redis
from sqlalchemy import select
from sqlalchemy.orm import Session
from telebot import TeleBot
from telebot.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

# My Stuff
from credentials import (
    BOT_TOKEN,
    REDIS_DB,
    REDIS_HOST,
    REDIS_PORT,
)
from db.connection import db_engine
from db.models import (
    Athlete,
    Race,
    RaceClass,
    ReplaceName,
    User,
)
from rating_bot.race_file_parse import (
    merge_athletes,
    parse_csv,
)
from rating_bot.results import (
    all_time_report,
    plases_rating,
    race_report,
)

bot = TeleBot(BOT_TOKEN)
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


def user_is_admin(message: Message) -> bool:
    with Session(db_engine) as session:
        user = session.get(User, message.from_user.id)
        if not user:
            return False
        else:
            return True


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
    filename = all_time_report()
    with open(filename, "r") as csvfile:
        bot.send_document(
            chat_id=message.chat.id,
            document=csvfile,
        )


@bot.message_handler(
    commands=["races"],
    chat_types=["private"],
    func=user_is_admin,
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
    plases_rating(race_id)
    filename = race_report(race_id=race_id)
    with open(filename, "r") as csvfile:
        bot.send_document(
            chat_id=callback_query.message.chat.id,
            document=csvfile,
        )

    bot.reply_to(callback_query.message, "Рейтинг сформирован")


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


if __name__ == "__main__":
    bot.infinity_polling()
