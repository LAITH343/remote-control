import sys
import logging
from datetime import datetime
from aiogram import Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Handlers import get_file, main_menu, system_menu
from config import bot, bot_owner, lh_logger

logging.basicConfig(level=logging.INFO)
# create memory storage for dispatcher
storage = MemoryStorage()
# Initialize bot and dispatcher
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(lambda message: message.from_user.id != bot_owner)
async def access_filter():
    pass


@dp.message_handler(lambda message: message.text in ['/help', '/Help', '/h', 'h', 'help', 'Help'])
async def help_message(message: types.Message):
    await message.answer(f"""
Welcome {message.from_user.first_name}
to get started using the bot send /start menu with options will apper below 
command explaining 
1. get file - allow you to get file from your computer by browsing the folder and select the file to upload
2. system control - show system control commands 
3. take screen shot - get screen shot from your computer and upload it
4. shutdown - power off your computer you can use it with to power off after specific minutes
            for example 'shutdown 5' will turn computer off after 5 minutes
5. reboot - restart your computer you can use it with to restart after specific minutes
            for example 'reboot 5' will restart the computer after 5 minutes

6. cancel scheduled shutdown/reboot - will cancel scheduled shutdown/reboot
7. running programs - send you list of current running programs
8. terminate program - force stop running program
9. battery level - send you battery level (Laptop)
10. is charger connected - check if the computer connected to charger/power or not
11. exit - close the menu
12. /poweroff - turn the bot off 
13. /help or help - to show this message
""")


if __name__ == '__main__':
    if sys.version_info < (3, 7):
        print("your python version is not supported\nyou need version 3.7 or higher")
        sys.exit(0)
    try:
        main_menu.setup(dp)
        get_file.setup(dp)
        system_menu.setup(dp)
    except Exception as e:
        lh_logger(f"{datetime.today()}\n{e}")
        print("error occurred check '.logs' file for more information")
    executor.start_polling(dp, skip_updates=True)
