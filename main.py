import os
import asyncio
from dotenv import load_dotenv

from client import Client
from bot import Bot
from wavelinkBot import WavelinkBot

def runClient(token, intents):
    client = Client(intents=intents)
    client.run(token)

async def runBot(bot):
    await load_extensions(bot)
    
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    
    await bot.start(token)
    
async def load_extensions(bot: Bot):
    for filename in os.listdir('./cogs'): #for every file in cogs
        if filename.endswith('.py'): #if the file is a python file
            #print(f'cogs.{filename[:-3]}')
            await bot.load_extension(f'cogs.{filename[:-3]}') #load the extension

async def main():
    bot = Bot()
    #runClient(token, intents)
    #bot = WavelinkBot()
    async with bot:
        await runBot(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
    