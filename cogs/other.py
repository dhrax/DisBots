from discord.ext import commands

class Other(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "test", description = "test command")
    async def test(self, ctx):
        await ctx.channel.send("test123")

async def setup(bot): # this is called by Pycord to setup the cog
    await bot.add_cog(Other(bot)) # add the cog to the bot