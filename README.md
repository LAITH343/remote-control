# Pc Remote Control via Telegram

It's telegram bot built with python and aiogram framework to help you control your computer from everywhere using telegram


## Installation

1. you need to install python 3.7 or higher on your computer
[python offical website](https://www.python.org/)

2. after installing python if you have git installed you can clone the repo by running
```bash
git clone repo-url
```

if you don't have git you can download it from [here](zip-file-url) (shortcut to repo download option) then extract it

3. open the folder using your files explorere then if your using Linux, Mac or Windows 10 or higher right click and select (open terminal here)/(open in terminal) if your using Windows 7 press Shift and right click, and you should see open with powershell or something like that

4. download the packages needed using
```bash
pip3 install -r requirements.txt
```

Note: if python3 or pip3 didn't work try using py or python and pip instead

5. create your bot using [BotFather](https://t.me/BotFather) and get your token you can find it below this message (Use this token to access the HTTP API:)

open `.env` file using your file editor and replace 'BOT TOKEN' with your token then save and exit

6. run id getter to get your account id by running
```bash
python3 id_getter.py
```

when you see `Updates were skipped successfully.` apper send /start or and message and the bot will respond with your account id
copy the id and back to the terminal/cmd and press Ctrl + C then open `.env` file with your text editor and replace OWNER_ID with your id then save and exit

now all Done, any time you want to run the bot follow step 3 and run
```bash
python3 main.py
```

## Author

[@LAITH343](https://github.com/LAITH343)
