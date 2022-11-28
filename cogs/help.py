import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Help(bot))