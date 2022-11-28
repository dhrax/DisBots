import discord
from discord.ext import commands

class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "val", description = "Val command")
    async def val(self, ctx):
        await ctx.channel.send("Siempre putita tu")
        await ctx.channel.send("Y COHINITAAAA")
        await ctx.channel.send("pero liquito bueno")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Greetings(bot)) # add the cog to the bot