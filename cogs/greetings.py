from discord.ext import commands

import datetime

class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "hello", description = "Say hello to the bot")
    async def hello(self, ctx):
        print(f"mensaje recibido a las {datetime.datetime.now()}")
        await ctx.channel.send("Hey!")
        print(f"mensaje enviado a las {datetime.datetime.now()}")

async def setup(bot): # this is called by Pycord to setup the cog
    await bot.add_cog(Greetings(bot)) # add the cog to the bot