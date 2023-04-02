from discord.ext import commands
import discord

class Bot(commands.Bot):
    
    def __init__(self, command_prefix = '!', self_bot = False):
        intents = discord.Intents.all()
        intents.messages = True
        commands.Bot.__init__(self, command_prefix = command_prefix, intents = intents, self_bot = self_bot)

    async def on_ready(self):
        print(f'{self.user} is ready and online!')
        
    async def on_command_error(self, ctx, exception) -> None:
        print(f'exception in command {ctx.command}: {exception}')
        if ctx.command == None:
            await ctx.channel.send(f'{exception}')
        return await super().on_command_error(ctx, exception)
    