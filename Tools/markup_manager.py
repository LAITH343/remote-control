from aiogram import types


def custom_markup(options: list):
    custom = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    for option in options:
        custom.add(option)
    return custom


def main_menu_markup():
    main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    options = ['get file', 'system control', 'exit']
    for option in options:
        main_menu.add(option)
    return main_menu


def system_control_markup():
    system_control = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    options = ['take screen shot', 'shutdown',
               'cancel scheduled shutdown/reboot',
               'reboot', 'running programs',
               'terminate program', 'battery level',
               'is charger connected', 'back to main menu']
    for option in options:
        system_control.add(option)
    return system_control
