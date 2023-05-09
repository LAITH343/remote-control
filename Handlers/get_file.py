from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from Tools.folder_navigator import Navigator
from config import bot, Platform
from Tools.markup_manager import main_menu_markup
import os

folder_browser = Navigator(Platform.default_path)


class CurrentLocation(StatesGroup):
    current_dir = State()


async def upload_file(message, file, state):
    if os.path.getsize(file) > 50000000:
        await message.answer("unable to upload (Telegram Limit)\nthe file size is grater than 50MB")
    else:
        await message.answer("uploading...")
        await bot.send_document(message.chat.id, document=open(file, 'rb'))
        await state.finish()
        await message.answer("back to main menu", reply_markup=main_menu_markup())


async def start_navigator(message: types.Message):
    await message.answer("navigate to the file or send full file/folder path")
    await folder_browser.show_content(message)
    await CurrentLocation.current_dir.set()


async def upload_browse(message: types.Message, state: FSMContext):
    path = await folder_browser.get_cd()
    if os.path.isfile(message.text):
        if os.path.getsize(message.text) == 0:
            await message.answer("cannot upload, file is empty")
        else:
            await upload_file(message, message.text, state)
    elif os.path.isfile(path + Platform.path_separator + message.text):
        if os.path.getsize(path + Platform.path_separator + message.text) == 0:
            await message.answer("cannot upload, file is empty")
        else:
            await upload_file(message, path + Platform.path_separator + message.text, state)
    elif os.path.isdir(path + Platform.path_separator + message.text) or os.path.isdir(message.text):
        await folder_browser.next(message, message.text)
    else:
        await message.answer("unknown file or folder")


async def exit(message: types.Message, state: FSMContext):
    await message.answer("Done", reply_markup=main_menu_markup())
    await state.finish()


async def back(message: types.Message):
    await folder_browser.back(message)


def setup(dp: Dispatcher):
    dp.register_message_handler(start_navigator, text='get file')
    dp.register_message_handler(exit, text="-->> Exit <<--", state=CurrentLocation.current_dir)
    dp.register_message_handler(back, text="-->> Back <<--", state=CurrentLocation.current_dir)
    dp.register_message_handler(upload_browse, state=CurrentLocation.current_dir)
