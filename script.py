# Telethon utility #pip install telethon
from telethon import TelegramClient, events
from telethon.tl.custom import Button

import configparser # Library for reading from a configuration file, # pip install configparser

import random # pip install random
from random import randint

import datetime # Library that we will need to get the day and time, #pip install datetime
import requests # Library used to make requests to external services (the weather forecast one) # pip install requests


#### Access credentials
config = configparser.ConfigParser() # Define the method to read the configuration file
config.read('config.ini') # read config.ini file

api_id = config.get('default','api_id') # get the api id
api_hash = config.get('default','api_hash') # get the api hash
BOT_TOKEN = config.get('default','BOT_TOKEN') # get the bot token
weather_key = config.get('default','weather_key') # read the key for the weather forecasts

# Create the client and the session called session_master. We start the session as the Bot (using bot_token)
client = TelegramClient('sessions/session_master', api_id, api_hash).start(bot_token=BOT_TOKEN)

# Define the /start command
@client.on(events.NewMessage(pattern='/(?i)start')) 
async def start(event):
    sender = await event.get_sender()
    SENDER = sender.id
    text = "Quiz Bot 🤖 ready\n" +\
        "\"<b>/time</b>\" → Find out what day it is, i'll even tell you the time!\n"+\
        "\"<b>/weather CITY</b>\" → I will provide the weather forecast for the city you entered\n" +\
        "\"<b>/quiz</b>\" → Let's play together!\n" 
    await client.send_message(SENDER, text, parse_mode="HTML")



### First command, get the time and day
@client.on(events.NewMessage(pattern='/(?i)time')) 
async def time(event):
    # Get the sender of the message
    sender = await event.get_sender()
    SENDER = sender.id
    # Define the text and send the message
    text = "Received! Day and time: " + str(datetime.datetime.now())
    await client.send_message(SENDER, text, parse_mode="HTML")




### Command to get the weather
@client.on(events.NewMessage(pattern='/(?i)weather')) 
async def weather(event):

    # Get the sender of the message
    sender = await event.get_sender()
    SENDER = sender.id

    try: 

        # In this way, if the user send for example /weather new york , new york will be selected as the CITY
        msg = event.message.text # /weather new york
        after_command = msg.split(" ")[1:] # ['/weather', 'new', 'york']
        city = ' '.join(after_command) # we get 'new york' 

        # Define the URL to make the request
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + weather_key + "&q=" + city

        # Get response and parse it to JSON format
        response = requests.get(complete_url)
        json_weather = response.json() 

        # If we get a good response, we send a specific message
        if json_weather["cod"] != "404":
            pred = json_weather['weather'][0]['main']
            desc = json_weather['weather'][0]['description']
            text = "Currently the weather in " + city + " is <b>" + str(pred) +"</b>, more specifically: <b>"+desc+"</b>"
            await client.send_message(SENDER, text, parse_mode="HTML")

    # Otherwhise we set a default message
        else:
            await client.send_message(SENDER, "I couldn't find the city....", parse_mode="HTML")

    # If the user just send the /weather commandi without a CITY, we get and Exeption
    except:
        await client.send_message(SENDER, "Insert a city after the /weather command!", parse_mode="HTML")
        return 
    
    

  
## Function that waits user event [press button]
def press_event(user_id):
    return events.CallbackQuery(func=lambda e: e.sender_id == user_id)


### Quiz command
@client.on(events.NewMessage(pattern='/(?i)quiz')) 
async def quiz(event):
    # get the sender
    sender = await event.get_sender()
    SENDER = sender.id

    # Start a conversation
    async with client.conversation(await event.get_chat(), exclusive=True) as conv:
        # get two random numbers between 1 and 10
        rand1 = randint(1,10)
        rand2 = randint(1,10)
        # make the sum
        sum = rand1+rand2
        # make another sum based on two different random numbers. This will be used for the wrong option
        sum_not_true = randint(1,10) + randint(1,10)

        # To make the position of the button random, let's define two keyboard that activates with 50% probability
        if(bool(random.getrandbits(1))):
            keyboard = [[Button.inline("{}".format(sum), sum)], [Button.inline("{}".format(sum_not_true), sum_not_true)]]
        else:
            keyboard = [[Button.inline("{}".format(sum_not_true), sum_not_true)],[Button.inline("{}".format(sum), sum)]]

        text = "<b>Quiz time</b> 🤖\n{} + {} = ?\n".format(str(rand1), str(rand2))
        await conv.send_message(text, buttons=keyboard, parse_mode='html')
        press = await conv.wait_event(press_event(SENDER))
        choice = str(press.data.decode("utf-8"))

        if(choice == str(sum)):
            await conv.send_message("Correct Answer!", parse_mode='html')
        else:
            await conv.send_message("Nope, i won!", parse_mode='html')

        await conv.cancel_all()
        return 



### MAIN
if __name__ == '__main__':
    print("bot started")
    client.run_until_disconnected()
