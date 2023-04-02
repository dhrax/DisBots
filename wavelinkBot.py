import discord
from discord.ext import commands
import wavelink

class WavelinkBot(commands.Bot):

    def __init__(self) -> None:
        intents = discord.Intents.all()
        intents.message_content = True

        super().__init__(intents=intents, command_prefix='!')

    async def on_ready(self) -> None:
        print(f'Logged in {self.user} | {self.user.id}')

    async def setup_hook(self) -> None:
        print('setup_hook called')
        node: wavelink.Node = wavelink.Node(uri='http://localhost:2333', password='youshallnotpass')
        await wavelink.NodePool.connect(client=self, nodes=[node])