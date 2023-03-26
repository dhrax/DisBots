from discord.ext import commands

class Other(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "val", description = "Val command")
    async def val(self, ctx):
        await ctx.channel.send("Siempre putita tu")
        await ctx.channel.send("Y COHINITAAAA")
        await ctx.channel.send("pero liquito bueno")

async def setup(bot): # this is called by Pycord to setup the cog
    await bot.add_cog(Other(bot)) # add the cog to the bot