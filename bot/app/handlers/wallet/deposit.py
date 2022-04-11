###############################
# WALLET:DEPOSIT handler      #
###############################

# Import libs
from aiogram import types
from aiogram.types import Message, InputFile, CallbackQuery
from aiogram.dispatcher.filters import Command,Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import *
from aiogram.dispatcher.filters.state import StatesGroup, State

# Import app modules
from .menu import *
from app.db.api import *
from app.utils.qiwi import *
from app.utils.logging import *
from app.settings import *
from app.loader import dp, bot

# STATES
class InputTicketCode(StatesGroup):
    Code = State()

#
@dp.callback_query_handler(text_contains="deposit")
async def root(call: CallbackQuery):
    text = settings.WALLET_DEPOSIT_TEXT
    name = call.message.chat.full_name
    # Лог сообщение
    logger.info(f"{name}:wallet:deposit")
    # Закрываем коллбэк
    await call.answer(cache_time=1)
    # Отправляем сообщение пользователю
    await call.message.edit_text(text=text, reply_markup=deposit_menu())


# PROVIDER TICKET
async def provider_ticket_page(callback: CallbackQuery, provider, **kwargs):
    await InputTicketCode.Code.set()
    text = settings.PROVIDER_TICKET_TEXT
    menu = back_menu("deposit")
    await callback.answer(cache_time=1, text=f"{settings.PROVIDER_TICKET_BUTTON}")
    await callback.message.reply(text, reply_markup=ticket_menu())

@dp.message_handler(state=InputTicketCode.Code)
async def send_message_confirm(message: types.Message, state: FSMContext):
    body = message.text
    logger.info(f"{body}")
    await bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)

@dp.callback_query_handler(state=InputTicketCode.Code)
async def reset_state(call: CallbackQuery, state: FSMContext):
    text = settings.WALLET_DEPOSIT_TEXT
    await state.reset_state()
    await call.answer(cache_ime=1)
    await call.message.edit_text(text=text, reply_markup=deposit_menu())

# PROVIDER QIWI
async def provider_qiwi_page(callback: CallbackQuery, provider, **kwargs):
    await bot.send_chat_action(chat_id=callback.message.chat.id, action="typing")
    text = settings.PROVIDER_QIWI_TEXT
    comment = gen_comment()
    form_url = create_form(comment=comment)
    menu = qiwi_menu(comment, form_url)
    await callback.answer(cache_time=1, text=f"{settings.PROVIDER_QIWI_BUTTON}")
    await callback.message.edit_text(text, reply_markup=menu)

async def check_payment(callback: CallbackQuery, provider, comment, **kwargs):
    check = check_payment_comment(comment)
    if check == False:
        await callback.answer(
            cache_time=1, text="Платеж в системе не найден", show_alert=True)
    else:
        uid = callback.message.chat.id
        customer = findUser(uid)
        customer_id = customer.id
        payment = makePayment(customer_id, check, "qiwi", comment)
        payment_id = int(payment['id'])
        confirmPayment(payment_id)
        text = "Ваш кошелек успешно пополнен!"
        await callback.answer(cache_time=1)
        await callback.message.edit_text(text=text, reply_markup=back_menu("start"))

# Навигатор
@dp.callback_query_handler(wallet_deposit_cd.filter())
async def deposit_navigate(call: CallbackQuery, callback_data: dict):
    logger.info(callback_data)
    current_level = callback_data.get("level")
    provider = callback_data.get("provider")
    comment = callback_data.get("comment")
    levels = {
        "1": provider_qiwi_page,
        "2": provider_ticket_page,
        "3": check_payment
    }
    current_level_function = levels[current_level]
    await current_level_function(
        call,
        provider=provider,
        comment=comment
    )






















