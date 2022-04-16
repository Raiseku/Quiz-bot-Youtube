# Quiz-bot-Youtube

The bot will be able to respond to the following commands:
/start will describe what the bot can do
/time will give the date and time of when that command was executed
/weather CITY will give the weather forecast for the entered city
/quiz will allow you to play a very simple quiz against the bot

_______________________________________________________
### HOW TO GET THE WEATHER FORECAST API

Get one at: https://openweathermap.org/api

Example request for weather forecast on the city of Rome: http://api.openweathermap.org/data/2.5/weather?appid=YOUR_APId&q=rome

Example Response
{
  "coord": {
    "lon": -85.1647,
    "lat": 34.257
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 298.25,
    "feels_like": 297.44,
    "temp_min": 297.13,
    "temp_max": 298.98,
    "pressure": 1019,
    "humidity": 24
  },
  "visibility": 10000,
  "wind": {
    "speed": 6.17,
    "deg": 130,
    "gust": 8.75
  },
  "clouds": {
    "all": 0
  },
  "dt": 1650050672,
  "sys": {
    "type": 2,
    "id": 2038061,
    "country": "US",
    "sunrise": 1650020953,
    "sunset": 1650067901
  },
  "timezone": -14400,
  "id": 4219762,
  "name": "Rome",
  "cod": 200
}


_______________________________________________________
### HOW TO GET API_ID AND API_HASH FOR TELETHON

Follow the instruction at: https://my.telegram.org/auth


_______________________________________________________
### HOW TO GET THE BOT_TOKEN

Write on telegram to @BotFather and follow the instruction

