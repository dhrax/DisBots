import discord
from discord.ext import commands

class Bot(commands.Bot):
    
    def __init__(self, command_prefix, intents, self_bot):
        commands.Bot.__init__(self, command_prefix = command_prefix, intents = intents, self_bot = self_bot)

    async def on_ready(self):
        print(f"{self.user} is ready and online!")
    