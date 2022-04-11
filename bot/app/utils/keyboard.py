from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

def make_btn(text, cdata):
    btn = InlineKeyboardButton(text=text,callback_data=cdata)
    return btn
