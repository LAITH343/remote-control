import os
import sys
import subprocess
from aiogram import Bot
import aiogram.utils.exceptions
from pathlib import Path


class Platform:
    isMac = sys.platform == "darwin"
    isLinux = sys.platform == "linux"
    isWindows = sys.platform == "win32"
    Unknown = isMac == isLinux == isWindows
    path_separator = '\\' if isWindows else '/'
    default_path = str(Path.home())
    if isWindows:
        isSuperUser = subprocess.run('openfiles', stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL).returncode == 0
    else:
        isSuperUser = subprocess.run('whoami', stdout=subprocess.PIPE).stdout.strip() == b'root'


if not os.path.isfile(".env"):
    print("pls create .env file first!")
    sys.exit()

cfg = open('.env', 'r')
data = cfg.readlines()[0:2]

if not data[0]:
    print("add bot token first!")

if not data[1] or not data[1].strip().isdigit():
    print("add admin user id first!")
    sys.exit()

bot_owner = int(data[1].strip())

bot_token = data[0].strip()
try:
    bot = Bot(token=bot_token)
except aiogram.utils.exceptions.ValidationError:
    print("Token is invalid, Enter valid one and try again")
    sys.exit(0)

path = Platform.default_path

if not os.path.isdir("./temp"):
    os.mkdir("temp")


def lh_logger(message: str):
    try:
        logs = open(".logs", 'a+')
        logs.write(message + '\n' if message[-1] != '\n' else message)
        logs.close()
    except Exception as e:
        print(f"failed to log: {message}\nError msg: {e}")
