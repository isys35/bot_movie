import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

import movie

load_dotenv()
TOKEN = os.environ.get("TOKEN")

if not TOKEN:
    raise Exception("Токен не найден")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать в бота-помощника по выбору фильма!")


@dp.message_handler(commands=["random", "help"])
async def send_random_movie(message: types.Message):
    movie_instance = movie.get_random_movie()
    await bot.send_message(message.chat.id, movie_instance)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
