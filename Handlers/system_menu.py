from aiogram import Dispatcher, types
from .system_controls.terminator import ProcessTerminating, terminate_program, cancel_terminating, terminating
from .system_controls.programs import get_running_programs
from .system_controls.display import take_screenshot
from .system_controls.power import power_off, cancel_power_off, reboot
from .system_controls.battery import get_battery_level, battery_status
from Tools.markup_manager import system_control_markup, main_menu_markup


async def menu(message: types.Message):
    await message.answer("you can control your pc via commands below", reply_markup=system_control_markup())


async def back_to_main(message: types.Message):
    await message.answer("back to main menu", reply_markup=main_menu_markup())


def setup(dp: Dispatcher):
    dp.register_message_handler(menu, text="system control")
    dp.register_message_handler(back_to_main, text="back to main menu")
    dp.register_message_handler(get_running_programs, text="running programs")
    dp.register_message_handler(terminate_program, text="terminate program")
    dp.register_message_handler(take_screenshot, text="take screen shot")
    dp.register_message_handler(power_off, regexp=r"^shutdown\s?\d*")
    dp.register_message_handler(cancel_power_off, text="cancel scheduled shutdown/reboot")
    dp.register_message_handler(reboot, regexp=r"^reboot\s?\d*")
    dp.register_message_handler(get_battery_level, text="battery level")
    dp.register_message_handler(battery_status, text="is charger connected")
    dp.register_message_handler(cancel_terminating, text="cancel", state=ProcessTerminating.pid)
    dp.register_message_handler(terminating, state=ProcessTerminating.pid)
