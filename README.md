# **Telegram Quiz Bot**

This Python project is a simple Telegram bot that can interact with users and provides the following functionalities:

- /start command: sends a welcome message with instructions about how to use the bot.
- /time command: returns the current date and time.
- /weather CITY command: returns the current weather for the specified city.
- /quiz command: starts a quiz with a single arithmetic operation (currently addition).

This bot was built using the following libraries:

- **`telethon`**: a Python 3 MTProto library to interact with Telegram's API.
- **`configparser`**: a library for reading from a configuration file.
- **`random`**: a library for generating random numbers.
- **`datetime`**: a library used to get the current date and time.
- **`requests`**: a library used to make requests to external services (in this case, the OpenWeatherMap API to retrieve weather data).

## **Getting started**

Before using the bot, you need to configure your access credentials in the **`config.ini`** file. You need to set the following parameters:

- **`api_id`**: your Telegram API ID.
- **`api_hash`**: your Telegram API hash.
- **`BOT_TOKEN`**: the token of your Telegram bot.
- **`weather_key`**: the API key for OpenWeatherMap.

You can obtain a Telegram API ID and hash by following the instructions **[here](https://core.telegram.org/api/obtaining_api_id)**. To obtain a bot token, you can talk to **[BotFather](https://telegram.me/botfather)** on Telegram. Finally, you can sign up for a free API key for OpenWeatherMap **[here](https://home.openweathermap.org/users/sign_up)**.

Once you have set up your credentials and installed all the libraries, you can run the script by executing **`python bot.py`**.
