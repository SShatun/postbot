"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import os

from aiogram import Bot, Dispatcher, executor, types

from insta import Insta

API_TOKEN = os.environ['TELEGRAM_TOKEN']
INSTA_PATTERN = "(?:(?:http|https):\/\/)?(?:www.)?(?:instagram.com|instagr.am|instagr.com)\/(\w+)"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi! Give me a link!")


@dp.message_handler(regexp=INSTA_PATTERN)
async def insta(message: types.Message):
    await Insta(message=message).get_data()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
