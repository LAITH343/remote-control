import psutil
import time
from PIL import Image
import os
from config import bot, lh_logger

try:
    import pyautogui
except KeyError:
    pass


async def screenshot(message) -> None:
    pyautogui.press('shift')
    time.sleep(1)
    screenshot = pyautogui.screenshot()
    # create an image from the raw data
    img = Image.frombytes("RGB", screenshot.size, screenshot.tobytes())
    img.save("screenshot.png")
    await bot.send_document(message.chat.id, document=open("screenshot.png", 'rb'))
    os.remove("screenshot.png")


async def battery_level() -> int:
    battery = psutil.sensors_battery()
    return battery.percent


async def battery_connected() -> bool:
    battery = psutil.sensors_battery()
    return battery.power_plugged


async def terminate_process(pid: int) -> bool:
    """
    return true if process terminated successfully
    """
    try:
        process = psutil.Process(pid)
        process.terminate()
        return True
    except Exception as e:
        lh_logger(f"error while terminating process\nError msg: {e}")
        return False


async def running_programs() -> bool:
    """
    return True if process done without issues
    """
    try:
        pids = psutil.pids()
        file = open('./temp/programs.txt', 'a+')
        file.write("name status pid\n")
        for pid in pids:
            process = psutil.Process(pid)
            file.write(f"{process.name()} {process.status()} {process.pid}\n")
        file.close()
        return True
    except Exception as e:
        lh_logger(f"Error while getting running programs info\nError msg: {e}")
        return False
