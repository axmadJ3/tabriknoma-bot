import asyncio
import logging
import sys
import dotenv
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.register import register_router

dotenv.load_dotenv()

TOKEN = getenv("BOT_TOKEN")

    
async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(
        register_router,
        )
    
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    