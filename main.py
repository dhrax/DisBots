import discord
from discord.ext import commands

from client import Client
from bot import Bot

import os
from dotenv import load_dotenv

def runClient(token, intents):
    client = Client(intents=intents)
    client.run(token)

def runBot(token, intents):
    bot = Bot(command_prefix='!', intents=intents, self_bot=False)

    for filename in os.listdir('./cogs'): #for every file in cogs
        if filename.endswith('.py'): #if the file is a python file
            print(f'cogs.{filename[:-3]}')
            bot.load_extension(f'cogs.{filename[:-3]}') #load the extension

    bot.run(token)

def main():
    load_dotenv()

    token = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    intents = discord.Intents.all()
    intents.messages = True

    #runClient(token, intents)
    runBot(token, intents)


if __name__ == "__main__":
    main()
    
    