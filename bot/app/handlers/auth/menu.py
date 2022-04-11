from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from money.money import Money
from money.currency import Currency

from app.settings import *
from app.db.api import *

def main_menu(balance):
    formated_balance = Money(balance, Currency.RUB).format('ru_RU')
    markup = InlineKeyboardMarkup(row_width=2)
    games = InlineKeyboardButton(
        text=settings.GAMES_BUTTON_TEXT, callback_data="games")
    wallet = InlineKeyboardButton(
        text=settings.WALLET_BUTTON_TEXT + f" ({formated_balance})", callback_data="wallet")
    faq = InlineKeyboardButton(
        text=settings.FAQ_BUTTON_TEXT, callback_data="faq")
    markup.add(games)
    markup.add(wallet)
    markup.add(faq)
    return markup






