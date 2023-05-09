from aiogram import types
import os
from Tools.markup_manager import custom_markup
from config import Platform


class Navigator:
    def __init__(self, current_location: str) -> None:
        self.path = current_location
        self.default_path = current_location

    async def show_content(self, message: types.Message):
        try:
            dir_content = os.listdir(self.path)
        except PermissionError:
            await message.answer("folder isn't accessible")
            self.path = Platform.path_separator.join(self.path.split(Platform.path_separator)[0:-1])
            dir_content = os.listdir(self.path)
        dir_content.append("-->> Back <<--")
        dir_content.append("-->> Exit <<--")
        await message.answer(f"current dir {self.path}", reply_markup=custom_markup(dir_content))

    async def next(self, message: types.Message, folder_path: str) -> None:
        if os.path.isdir(folder_path):
            self.path = folder_path
            await self.show_content(message)
        elif not os.path.isdir(self.path + Platform.path_separator + folder_path):
            await message.answer("folder not found")
        else:
            self.path += Platform.path_separator + folder_path
            await self.show_content(message)

    async def back(self, message: types.Message) -> None:
        self.path = Platform.path_separator.join(self.path.split(Platform.path_separator)[0:-1])
        await self.show_content(message)

    async def get_cd(self) -> str:
        return self.path
