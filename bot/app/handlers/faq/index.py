from aiogram import types
from aiogram.types import Message, InputFile, CallbackQuery
from aiogram.dispatcher.filters import Command,Text

from .menu import main_menu
from app.db.api import *
from app.utils.logging import *
from app.settings import *
from app.loader import dp, bot


@dp.callback_query_handler(text_contains="faq")
async def root(call: CallbackQuery):

    text = settings.FAQ_INDEX_TEXT

    name = call.message.chat.full_name

    # Лог сообщение
    logger.info(f"{name} - FAQ PAGE")

    # Закрываем коллбэк
    await call.answer(cache_time=1)
    # Отправляем сообщение пользователю
    await call.message.edit_text(text=text, reply_markup=main_menu())

























