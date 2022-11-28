import discord
from discord.ext import commands
import youtube_dl
from YTDLSource import YTDLSource

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.queue = {}

    async def addToQueue(self, ctx, guild, song):
        if guild.id in self.queue:
            self.queue[guild.id] = []

        self.queue[guild.id].append(song)

        await ctx.send(f"Song added to queue: {song}")


    async def playSong(self, ctx, channel, URL):
        async with ctx.typing():
            song = self.queue[channel.guild.id].pop(0, None)
            if song == None:
                return
            
            channel.play(discord.FFmpegPCMAudio(URL, **YTDLSource.ffmpeg_play_options))
        
        await ctx.send('**Now playing:** {}'.format(URL))

    @commands.command(name='join', help='Tells the bot to join the voice channel')
    async def join(self, ctx):
        if not ctx.message.author.voice:
            await ctx.channel.send(f'{ctx.message.author.name} is not connected to any voice channel')
            return
        else:
            channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command(name='leave', help='Tells the bot leave the voice channel')
    async def leave(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client != None and voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.channel.send("The bot is not connected to a voice channel.")

    @commands.command(name='play', help='Tells the bot to play song')
    async def play(self, ctx: commands.Context, url):
        try :

            server = ctx.message.guild
            
            if server.voice_client == None:
                await ctx.invoke(self.join)

            voice_channel = server.voice_client
            
            with youtube_dl.YoutubeDL(YTDLSource.ytdl_format_options) as ydl:
                info = ydl.extract_info(url, download=False)
                URL = info['formats'][0]['url']
                #voice_channel.play(discord.FFmpegPCMAudio(URL, **YTDLSource.ffmpeg_play_options))
                await self.addToQueue(ctx, server, URL)
                await self.playSong(ctx, voice_channel, URL)

            #await ctx.channel.send(f'**Now playing:** {url}')
        except Exception as e:
            print(e)
            await ctx.channel.send(f"An exception has been thrown: {e}")

    @commands.command(name='pause', help='Pauses the song playing at the moment')
    async def pause(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client != None and voice_client.is_playing():
            voice_client.pause()
        else:
            await ctx.channel.send("The bot is not playing anything at the moment.")
        
    @commands.command(name='resume', help='Resumes the song paused')
    async def resume(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client != None and voice_client.is_paused():
            voice_client.resume()
        else:
            await ctx.channel.send("The bot was not playing anything before this. Use !play command")

    @commands.command(name='stop', help='Stops the song playing at the moment')
    async def stop(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client != None and voice_client.is_playing():
            voice_client.stop()
        else:
            await ctx.channel.send("The bot is not playing anything at the moment.")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Music(bot)) # add the cog to the bot