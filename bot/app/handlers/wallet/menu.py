from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from app.settings import *
from app.db.api import *

def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    withdrawal = InlineKeyboardButton(
        text=settings.WALLET_WITHDRAWAL_BUTTON, callback_data="withdrawal"
    )
    deposit = InlineKeyboardButton(
        text=settings.WALLET_DEPOSIT_BUTTON, callback_data="deposit"
    )
    back = InlineKeyboardButton(
        text=settings.BACK_BTN, callback_data="start")
    markup.add(deposit, withdrawal)
    markup.add(back)
    return markup

wallet_deposit_cd = CallbackData('dep-nav', 'level', 'provider', 'comment')

def make_wallet_deposit_nav(level, provider=0, comment=0):
    return wallet_deposit_cd.new(level=level, provider=provider, comment=comment)

def deposit_menu():
    markup = InlineKeyboardMarkup(row_width=2)

    qiwi = InlineKeyboardButton(
        text=settings.PROVIDER_QIWI_BUTTON,
        callback_data=make_wallet_deposit_nav(
            level=1,
            provider="qiwi"))

    ticket = InlineKeyboardButton(
        text=settings.PROVIDER_TICKET_BUTTON,
        callback_data=make_wallet_deposit_nav(
            level=2,
            provider="ticket"))

    back = InlineKeyboardButton(
        text=settings.BACK_BTN, callback_data="wallet")

    markup.add(qiwi)
    markup.add(ticket)
    markup.add(back)
    return markup


def qiwi_menu(comment, url):
    markup = InlineKeyboardMarkup(row_width=2)
    back = InlineKeyboardButton(
        text=settings.CANCEL_BTN, callback_data="deposit")
    url_btn = InlineKeyboardButton(text=settings.PROVIDER_QIWI_PAY_BUTTON, url=url)
    check_btn = InlineKeyboardButton(
        text=settings.PROVIDER_QIWI_CHECK_BUTTON, callback_data=make_wallet_deposit_nav(level=3, provider="qiwi", comment=comment))
    markup.add(url_btn)
    markup.add(check_btn)
    markup.add(back)
    return markup


def ticket_menu():
    markup = ReplyKeyboardMarkup(row_width=2)
    back = KeyboardButton(text=settings.BACK_BTN)
    markup.add(back)
    return markup

def back_menu(cb):
    markup = InlineKeyboardMarkup(row_width=2)
    back = InlineKeyboardButton(
        text=settings.BACK_BTN, callback_data=cb)
    markup.add(back)
    return markup

def withdrawal_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    back = InlineKeyboardButton(
        text=settings.BACK_BTN, callback_data="wallet")
    markup.add(back)
    return markup

