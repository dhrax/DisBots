from discord.ext import commands

class Bot(commands.Bot):
    
    def __init__(self, command_prefix, intents, self_bot):
        commands.Bot.__init__(self, command_prefix = command_prefix, intents = intents, self_bot = self_bot)

    async def on_ready(self):
        print(f"{self.user} is ready and online!")
        
    async def on_command_error(self, context, exception) -> None:
        print(f'exception in command {context.command}: {exception}')
        return await super().on_command_error(context, exception)
    