from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from Tools.markup_manager import custom_markup, main_menu_markup
from Tools.system_controls import terminate_process
from aiogram import types


class ProcessTerminating(StatesGroup):
    pid = State()


async def terminate_program(message: types.Message):
    await message.answer("send program pid", reply_markup=custom_markup(['cancel']))
    await ProcessTerminating.pid.set()


async def terminating(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("program pid should be digits only")
        return
    if await terminate_process(int(message.text)):
        await message.answer("program terminated successfully", reply_markup=main_menu_markup())
    else:
        await message.answer("program terminating failed", reply_markup=main_menu_markup())
    await state.finish()


async def cancel_terminating(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("canceled", reply_markup=main_menu_markup())
