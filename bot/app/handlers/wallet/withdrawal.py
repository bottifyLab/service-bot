from aiogram import types
from aiogram.types import Message, InputFile, CallbackQuery
from aiogram.dispatcher.filters import Command,Text

from .menu import withdrawal_menu
from app.db.api import *
from app.utils.logging import *
from app.settings import *
from app.loader import dp, bot


@dp.callback_query_handler(text_contains="withdrawal")
async def root(call: CallbackQuery):

    text = settings.WALLET_WITHDRAWAL_TEXT

    name = call.message.chat.full_name

    # Лог сообщение
    logger.info(f"{name} - WALLET WITHDRAWAL PAGE")

    # Закрываем коллбэк
    await call.answer(cache_time=1)
    # Отправляем сообщение пользователю
    await call.message.edit_text(text=text, reply_markup=withdrawal_menu())

























