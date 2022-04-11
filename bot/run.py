from app.bot import *

import app.handlers
import app.proxies

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

