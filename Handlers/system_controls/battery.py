from Tools.system_controls import battery_level, battery_connected
from aiogram import types
from config import lh_logger


async def get_battery_level(message: types.Message):
    try:
        level = await battery_level()
        await message.answer(f"Battery level is {level}%")
    except Exception as e:
        lh_logger(f"failed to get battery level\nError msg: {e}")
        await message.answer("somthing went wrong\ncheck '.log' for more information")


async def battery_status(message: types.Message):
    try:
        if await battery_connected():
            await message.answer("charger connected")
        else:
            await message.answer("charger not connected")
    except Exception as e:
        lh_logger(f"failed to get charging status\nError msg: {e}")
        await message.answer("somthing went wrong\ncheck '.log' for more information")

