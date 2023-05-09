from aiogram import types
from config import Platform, lh_logger
import os
import subprocess


async def power_off(message: types.Message):
    if len(message.text.split()) > 2:
        await message.answer("pls send the command with one number\nExample: shutdown 10")
        return
    if len(message.text.split()) > 1:
        time_min = int(message.text.split()[-1])
    else:
        time_min = 0
    try:
        if Platform.isLinux:
            if not Platform.isSuperUser:
                await message.answer("can't do this action\nbot need admin privileges to do it")
            else:
                await message.answer(f"pc is going off after {time_min} minutes", reply_markup=types.ReplyKeyboardRemove())
                os.system(f"sudo shutdown -P {time_min}")
        elif Platform.isMac:
            # not tested
            if not Platform.isSuperUser:
                await message.answer("can't do this action\nbot need admin privileges to do it")
            else:
                await message.answer(f"pc is going off after {time_min} minutes", reply_markup=types.ReplyKeyboardRemove())
                os.system(f"sudo shutdown -P +{time_min}")
        elif Platform.isWindows:
            await message.answer(f"pc is going off after {time_min} minutes", reply_markup=types.ReplyKeyboardRemove())
            os.system(f"shutdown /s /t {time_min * 60}")
    except Exception as e:
        lh_logger(f"couldn't shutdown\nError msg: {e}")
        await message.answer(f"something went wrong\ncheck '.logs' for more information")


async def cancel_power_off(message: types.Message):
    try:
        if Platform.isLinux:
            if os.path.isfile("/run/systemd/shutdown/scheduled"):
                os.system("shutdown -c")
                if not os.path.isfile("/run/systemd/shutdown/scheduled"):
                    await message.answer("scheduled shutdown/reboot canceled")
                else:
                    await message.answer("failed to cancel scheduled shutdown/reboot")
            else:
                await message.answer("there's no scheduled shutdown/reboot")
        elif Platform.isMac:
            # not tested
            check = subprocess.Popen(['pmset', '-g', 'sched'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = check.stdout.read().decode('utf-8')
            if 'Scheduled Shutdown:' in output:
                os.system("sudo pmset -a cancel")
                new_check = subprocess.Popen(['pmset', '-g', 'sched'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if 'Scheduled Shutdown:' not in new_check.stdout.read().decode('utf-8'):
                    await message.answer("scheduled shutdown/reboot canceled")
                else:
                    await message.answer("failed to cancel scheduled shutdown/reboot")
            else:
                await message.answer("there's no scheduled shutdown/reboot")
        elif Platform.isWindows:
            return_code = os.system("shutdown /a 2>NUL")
            if return_code == 0:
                await message.answer("scheduled shutdown/reboot canceled")
            else:
                await message.answer("there's no scheduled shutdown/reboot")
    except Exception as e:
        lh_logger(f"couldn't cancel shutdown\nError msg: {e}")
        await message.answer(f"something went wrong\ncheck '.logs' for more information")


async def reboot(message: types.Message):
    if len(message.text.split()) > 2:
        await message.answer("pls send the command with one number\nExample: reboot 10")
        return
    if len(message.text.split()) > 1:
        time_min = int(message.text.split()[-1])
    else:
        time_min = 0
    try:
        if Platform.isLinux:
            if not Platform.isSuperUser:
                await message.answer("can't do this action\nbot need admin privileges to do it")
            else:
                await message.answer(f"pc is going to reboot after {time_min} minutes", reply_markup=types.ReplyKeyboardRemove())
                os.system(f"sudo shutdown -r +{time_min}")
        elif Platform.isMac:
            # not tested
            if not Platform.isSuperUser:
                await message.answer("can't do this action\nbot need admin privileges to do it")
            else:
                await message.answer(f"pc is going to reboot after {time_min} minutes", reply_markup=types.ReplyKeyboardRemove())
                os.system(f"sudo shutdown -r +{time_min}")
        elif Platform.isWindows:
            await message.answer(f"pc is going to reboot after {time_min} minutes", reply_markup=types.ReplyKeyboardRemove())
            os.system(f"shutdown /r /t {time_min * 60}")
    except Exception as e:
        lh_logger(f"couldn't reboot\nError msg: {e}")
        await message.answer(f"something went wrong\ncheck '.logs' for more information")
