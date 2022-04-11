from pydantic import BaseSettings

from .db.api import *

class Settings(BaseSettings):
    # BOT SETTINGS
    BOT_TOKEN: str = ''
    ADMIN_ID: str = ''
    LOGS_CHANNEL_ID: str = ''

    # QIWI SETTINGS
    QIWI_TOKEN: str = ''
    QIWI_P2P_PUBLIC: str = ''
    QIWI_P2P_SECRET: str = ''

    # GAMES MODULE ENVS
    GAMES_INDEX_TEXT: str = "This text getting from settings.py"
    GAMES_BUTTON_TEXT: str = "GAMES_BUTTON_TEXT"

    # WALLET MODULE ENVS
    WALLET_INDEX_TEXT: str = "This text getting from settings.py"
    WALLET_BUTTON_TEXT: str = "WALLET_BUTTON_TEXT"
    WALLET_DEPOSIT_BUTTON: str = "WALLET_DEPOSIT_BUTTON"
    WALLET_DEPOSIT_TEXT: str = "This text getting from settings.py"
    WALLET_WITHDRAWAL_BUTTON: str = "WALLET_WITHDRAWAL_BUTTON"
    WALLET_WITHDRAWAL_TEXT: str = "This text getting from settings.py"

    PROVIDER_QIWI_TEXT: str = "Qiwi-provider"
    PROVIDER_QIWI_BUTTON: str = "QIWI"
    PROVIDER_QIWI_CHECK_BUTTON: str = "check"
    PROVIDER_QIWI_PAY_BUTTON: str = "pay"

    PROVIDER_TICKET_BUTTON: str = "Ticket"
    PROVIDER_TICKET_TEXT: str = "Ticket-provider"

    # FAQ MODULE ENVS
    FAQ_INDEX_TEXT: str = "This text getting from settings.py"
    FAQ_BUTTON_TEXT: str = "FAQ_BUTTON_TEXT"

    # AUTH MODULE ENVS
    AUTH_INDEX_TEXT: str = "This text getting from settings.py"
    AUTH_STICKER_FILE_ID: str = "CAACAgIAAxkBAAEEDUtiIjyA-0WrcIrdX-T3oxlnhYobzAAC6RcAAqcXEUmcFnIOrr3gxSME"
    # BUTTONS
    MAIN_PAGE_BTN: str = "MAIN PAGE BUTTON"

    MAIN_COVER_TEXT: str = 'change MAIN_COVER_TEXT'
    MAIN_TEXT: str = 'change MAIN_TEXT'

    SUB_LIST_BTN: str = 'SUB_LIST_BTN'
    SUB_LIST_TEXT: str = '<b>Самый отборный контент по категориям - выбери нужную</b>'

    USER_SUBS_BTN: str = 'change USER_SUBS_BTN'
    USER_SUBS_TEXT: str = 'change USER_SUBS_TEXT'

    GET_ACCESS_TEXT: str = '🔐 Получить доступ'

    BILL_INFO_TEXT: str = '<code>🗯 Оплатите доступ к тарифу удобным способом. После оплаты нажмите "Проверить оплату"\n</code>'
    PAY_URL_BTN: str = '🔗 Оплатить доступ'
    CHECK_PAY_BTN: str = '🔃 Проверить оплату'

    BACK_BTN: str = '↩️ Назад'
    CONFIRM_BTN: str = '✅ Да'
    CANCEL_BTN: str = '❌ Отмена'

settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)

