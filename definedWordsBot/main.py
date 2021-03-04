from aiogram import Bot, Dispatcher, executor
import asyncio

from config import bot_token

loop = asyncio.get_event_loop()
bot = Bot(bot_token, parse_mode="HTML")
dp = Dispatcher(bot, loop)

if __name__ == "__main__":
    from handlers import dp

    executor.start_polling(dp)
