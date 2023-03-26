import discord
import os
import asyncio
from dotenv import load_dotenv

from client import Client
from bot import Bot

def runClient(token, intents):
    client = Client(intents=intents)
    client.run(token)

async def runBot(token, bot):
    await load_extensions(bot)

    await bot.start(token)
    
async def load_extensions(bot: Bot):
    for filename in os.listdir('./cogs'): #for every file in cogs
        if filename.endswith('.py'): #if the file is a python file
            print(f'cogs.{filename[:-3]}')
            await bot.load_extension(f'cogs.{filename[:-3]}') #load the extension

async def main():
    load_dotenv()

    token = os.getenv('DISCORD_TOKEN')
    #GUILD = os.getenv('DISCORD_GUILD')

    intents = discord.Intents.all()
    intents.messages = True

    #runClient(token, intents)
    
    bot = Bot(command_prefix='!', intents=intents, self_bot=False)
    async with bot:
        await runBot(token, bot)

if __name__ == "__main__":
    asyncio.run(main())
    
    