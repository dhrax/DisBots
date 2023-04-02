from discord.ext import commands
import wavelink

class WavelinkMusic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.queue = {}
        
    @commands.command(name='wvplay')
    async def wvPlay(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
        vc: wavelink.Player = ctx.voice_client
        print(f'Node ready: {wavelink.NodePool.get_node().status}')
        
        player: wavelink.Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=wavelink.Player, context=ctx)
        if not vc: # check if the bot is not in a voice channel
            vc = await ctx.author.voice.channel.connect(cls=wavelink.Player) # connect to the voice channel
        await vc.set_volume(int(500))
        track = await wavelink.YouTubeTrack.search(search, return_first=True)
        
        await vc.play(track)
        await ctx.send(f'**Now playing:** {track.title}')
        
        
    @commands.command(name='wvjoin', help='Tells the bot to join the voice channel')
    async def join(self, ctx):
        if not ctx.message.author.voice:
            await ctx.channel.send(f'{ctx.message.author.name} is not connected to any voice channel')
            raise commands.CommandError("Author not connected to a voice channel.")
        else:
            await ctx.message.author.voice.channel.connect()

    @wvPlay.before_invoke
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
            
    @commands.Cog.listener()
    async def on_wavelink_node_ready(node: wavelink.Node) -> None:
        print(f"Node {node.id} is ready!")
        
    async def cog_command_error(self, ctx: commands.Context, error: Exception):
        """Cog wide error handler."""
        print(error)

async def setup(bot): # this is called by Pycord to setup the cog
    await bot.add_cog(WavelinkMusic(bot)) # add the cog to the bot