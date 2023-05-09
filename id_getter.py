import sys

import aiogram.utils.exceptions
from aiogram import Dispatcher, executor, types, Bot

env = open('.env', 'r')
token = env.readlines()[0].strip()
if token == "":
    print("add token first!")
    sys.exit(0)
try:
    bot = Bot(token=token)
except aiogram.utils.exceptions.ValidationError:
    print("Token is invalid, Enter valid one and try again")
    sys.exit(0)

dp = Dispatcher(bot=bot)


@dp.message_handler()
async def send_id(message: types.Message):
    await message.answer(message.from_user.id)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
