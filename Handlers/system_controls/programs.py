import os
from aiogram import types
from Tools.system_controls import running_programs
from config import bot, lh_logger


async def get_running_programs(message: types.Message):
    if await running_programs():
        try:
            await bot.send_document(chat_id=message.chat.id, document=open('./temp/programs.txt', 'rb'))
            os.remove("./temp/programs.txt")
        except Exception as e:
            lh_logger(f"sending running programs failed\nError msg: {e}")
    else:
        await message.answer("failed to get running programs\ncheck '.logs' for more information")

