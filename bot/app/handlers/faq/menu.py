from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from app.settings import *
from app.db.api import *

def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)

    back = InlineKeyboardMarkup(
        text=settings.BACK_BTN, callback_data="start")

    markup.add(back)
    return markup






