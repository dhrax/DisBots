import discord
from discord.ext import commands
from YTDLSource import YTDLSource

class Download(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "download_song", description = "Download a youtube song")
    async def download_song(self, ctx, url):
        server = ctx.message.guild
        voice_channel = server.voice_client

        await ctx.channel.send(f'**Downloading song from:** {url}')

        #muestra el indicador de que el bot esta escribiendo
        async with ctx.typing():
            #download and play a song
            filename = await YTDLSource.from_url(url)
            #discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename)
        await ctx.channel.send('**Song downloaded:** {}'.format(filename))

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Download(bot)) # add the cog to the bot