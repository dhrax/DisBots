from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


async def setup(bot): # this is called by Pycord to setup the cog
    await bot.add_cog(Help(bot))