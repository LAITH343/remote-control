import asyncio
import sys
from Tools.markup_manager import main_menu_markup
from aiogram import Dispatcher, types
from config import lh_logger


async def show_menu(message: types.Message):
    await message.answer("Welcome, i'm Prct select option to get started!", reply_markup=main_menu_markup())


async def power_off_bot(message: types.Message):
    await message.answer("shutting down the bot\nBye", reply_markup=types.ReplyKeyboardRemove())
    try:
        asyncio.get_running_loop().stop()
        sys.exit()
    except SystemExit:
        pass
    except Exception as e:
        lh_logger(f"shutting down the bot failed\nError msg: {e}")
        await message.answer(f"something went wrong\ncheck '.logs' for more information")


async def exit(message: types.Message):
    await message.answer("see you later", reply_markup=types.ReplyKeyboardRemove())


def setup(dp: Dispatcher):
    dp.register_message_handler(show_menu, commands=['start'])
    dp.register_message_handler(power_off_bot, commands=['poweroff'])
    dp.register_message_handler(exit, text='exit')
