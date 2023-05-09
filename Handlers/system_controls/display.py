from aiogram import types
from Tools.system_controls import screenshot
import os


async def take_screenshot(message: types.Message):
    try:
        os.getenv('DISPLAY')
    except KeyError:
        await message.answer("Display not found")
        return
    await message.answer("taking screen shot... ")
    await screenshot(message)
