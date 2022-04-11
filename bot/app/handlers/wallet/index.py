###############################
# wallet module index handler #
###############################

# Import libs
from aiogram import types
from aiogram.types import Message, InputFile, CallbackQuery
from aiogram.dispatcher.filters import Command,Text

# Import app modules
from .menu import main_menu
from app.db.api import *
from app.utils.logging import *
from app.settings import *
from app.loader import dp, bot

# Callback handlers
@dp.callback_query_handler(text_contains="wallet")
async def root(call: CallbackQuery):
    text = settings.WALLET_INDEX_TEXT
    name = call.message.chat.full_name
    # Лог сообщение
    logger.info(f"{name}:wallet:index")
    # Закрываем коллбэк
    await call.answer(cache_time=1)
    # Отправляем сообщение пользователю
    await call.message.edit_text(text=text, reply_markup=main_menu())

























