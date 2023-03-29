from discord.ext import commands
from YTDLSource import YTDLSource
import asyncio

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.queue = {}
    
    async def addToQueue(self, ctx, guild, player):
        if guild.id not in self.queue:
            self.queue[guild.id] = []
        
        self.queue[guild.id].append(player)
        await ctx.send(f"Song added to queue: {player.title}")
        
    async def playSong(self, ctx, channel, player):
        async with ctx.typing():            
            channel.play(player, after= lambda e: asyncio.run_coroutine_threadsafe(self.playNext(ctx, channel), self.bot.loop))
            
            await ctx.send('**Now playing:** {}'.format(player.title))

    async def playNext(self, ctx: commands.Context, channel):
        guildId = ctx.message.guild.id
        if len(self.queue[guildId]) >= 1:
            player = self.queue[guildId].pop(0)
            await self.playSong(ctx, channel, player)
        else:
            await ctx.send("No more songs in queue.")
            await asyncio.sleep(15)
        if not channel.is_playing():
            asyncio.run_coroutine_threadsafe(channel.disconnect(ctx), self.bot.loop)
            asyncio.run_coroutine_threadsafe(ctx.send("No more songs in queue."), self.bot.loop)
    
    @commands.command(name='playQueue')
    async def playQueue(self, ctx: commands.Context):
        await self.playNext(ctx, ctx.voice_client)
        
    @commands.command(name='queue')
    async def addSongQueueCommand(self, ctx: commands.Context, url):
        song = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
        await self.addToQueue(ctx, ctx.message.guild, song)

    @commands.command(name='showQueue')
    async def showQueue(self, ctx: commands.Context):
        #add embed message
        guild = ctx.message.guild
        await ctx.send(f"{guild.name} song queue:")
        message = ''
        if guild.id in self.queue:
            for i, song in enumerate(self.queue[guild.id]):
                message += f'{i} {song.title}\n'
        await ctx.send(message if message else 'Empty list')
    
    
    @commands.command(name='join', help='Tells the bot to join the voice channel')
    async def join(self, ctx):
        if not ctx.message.author.voice:
            await ctx.channel.send(f'{ctx.message.author.name} is not connected to any voice channel')
            raise commands.CommandError("Author not connected to a voice channel.")
        else:
            await ctx.message.author.voice.channel.connect()
    
    @commands.command(name='play', help='Tells the bot to play song')
    async def play(self, ctx: commands.Context, url):
        try :
            voice_client = ctx.voice_client
            
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            await self.playSong(ctx, voice_client, player)

        except Exception as e:
            print(e)
            await ctx.channel.send(f"An exception has been thrown: {e}")
            
    @commands.command(name='stream', help='Tells the bot to streams from an url')
    async def stream(self, ctx, *, url):
        async with ctx.typing():                
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            await self.playSong(ctx, ctx.voice_client, player)

    @commands.command(name='pause', help='Pauses the song playing at the moment')
    async def pause(self, ctx):
        voice_client = ctx.voice_client
        if voice_client != None and voice_client.is_playing():
            voice_client.pause()
        else:
            await ctx.channel.send("The bot is not playing anything at the moment.")
        
    @commands.command(name='resume', help='Resumes the song paused')
    async def resume(self, ctx):
        voice_client = ctx.voice_client
        if voice_client != None and voice_client.is_paused():
            voice_client.resume()
        else:
            await ctx.channel.send("The bot was not playing anything before this. Use !play command to play a song")

    @commands.command(name='stop', help='Stops the song playing at the moment')
    async def stop(self, ctx):
        voice_client = ctx.voice_client
        if voice_client != None and voice_client.is_playing():
            voice_client.stop()
        else:
            await ctx.channel.send("The bot is not playing anything at the moment.")
            
    @commands.command(name='leave', help='Tells the bot leave the voice channel')
    async def leave(self, ctx):
        voice_client = ctx.voice_client
        if voice_client != None and voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.channel.send("The bot is not connected to a voice channel.")
            
    @play.before_invoke
    @stream.before_invoke
    @playQueue.before_invoke
    async def ensure_voice(self, ctx):
        '''
        Ensures access to a voice channel for the required commands
        '''
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.invoke(self.join)
            else:
                await ctx.channel.send(f'{ctx.message.author.name} is not connected to any voice channel')
                
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

async def setup(bot): # this is called by Pycord to setup the cog
    await bot.add_cog(Music(bot)) # add the cog to the bot