# Third Party Stuff
from sqlalchemy.orm import Session
from telebot import TeleBot
from telebot.types import Message

# My Stuff
from credentials import BOT_TOKEN
from db.connection import db_engine
from db.models import User

bot = TeleBot(BOT_TOKEN)
bot.delete_webhook()


def user_is_admin(message: Message) -> bool:
    with Session(db_engine) as session:
        user = session.get(User, message.from_user.id)
        if not user:
            return False
        else:
            return True
