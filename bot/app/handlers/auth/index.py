from aiogram import types
from aiogram.types import Message, InputFile, CallbackQuery
from aiogram.dispatcher.filters import Command,Text

from .menu import simple_menu
from app.db.api import *
from app.utils.logging import *
from app.settings import *
from app.loader import dp, bot

@dp.message_handler(commands=["start"], state="*")
async def start(message: Message):

    uid = message.chat.id
    name = message.chat.full_name
    text = settings.AUTH_INDEX_TEXT + f"====\n\nВаше имя: <code>{name}</code>"

    register = registerUser(uid,name)
    customer = findUser(uid)
    
    logger.info({'/': 'start', 'customer': register, 'user': name})

    await message.answer(text=text, reply_markup=simple_menu())


@dp.callback_query_handler(text_contains="start")
async def root(call: CallbackQuery):

    # Получаем id и имя от пользователя
    name = call.message.chat.full_name
    uid = call.message.chat.id
    id_link = f"<a href='tg://user?id={uid}'>{name}</a>"
    text = settings.AUTH_INDEX_TEXT + f"====\n\nВаше имя: <code>{name}</code>"
    customer = findUser(uid)

    # Лог сообщение
    logger.info(f"{name}:auth:index")

    # Закрываем коллбэк
    await call.answer(cache_time=1)

# Отправляем сообщение пользователю
    await call.message.edit_text(text=text, reply_markup=main_menu(customer.balance))

























