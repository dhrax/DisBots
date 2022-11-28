import discord
import random

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        response = None

        if str(message.author) == 'dhrax#4911':
            response = 'You are so cool'
        elif str(message.author) == 'Valery#1527':
            response = 'Eres bastante puta no?'
        elif str(message.author) == 'Luismichu#1612':
            response = 'No se puede ser peor al Hades'
        elif message.content == '!B99':
            brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
            ]

            response = random.choice(brooklyn_99_quotes)

        elif message.content.startswith("!ping"):
            response = "Pong!"
        
        if response != None:
            await message.channel.send(response)