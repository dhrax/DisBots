import discord
from discord.ext import commands

class Embed(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "embed", description = "testing formatted messages")
    async def embed(self, ctx):
        embed = discord.Embed(
                    title="My Amazing Embed",
                    description="Embeds are super easy, barely an inconvenience.",
                    color=discord.Colour.blue(), # Pycord provides a class with default colors you can choose from
                )
        embed.add_field(name="A Normal Field", value="A really nice field with some information. **The description as well as the fields support markdown!**")

        embed.add_field(name="Inline Field 1", value="Inline Field 1", inline=True)
        embed.add_field(name="Inline Field 2", value="Inline Field 2", inline=False)
        embed.add_field(name="Websites", value="[Daisa](https://daisaa.com/)", inline=False)

        embed.add_field(name = "Python code", value = """```python
                                                        import discord
                                                        class Bot()
                                                        print(Hello world!)
                                                        ```
                                                        """)
    
        embed.set_footer(text="Footer! No markdown here.") # footers can have icons too
        embed.set_author(name="Daisa", icon_url="https://daisaa.com/assets/v.png")
        embed.set_thumbnail(url="https://media-exp1.licdn.com/dms/image/C4D03AQEy5dw32qgQ8g/profile-displayphoto-shrink_400_400/0/1615148832899?e=1670457600&v=beta&t=OmYP2CRNnvDF8Bek969msIrx9npOHkGsKnaExlVrwWE")
        embed.set_image(url="https://static.wikia.nocookie.net/nuclear-throne/images/8/89/Character_YV_B.png/revision/latest/scale-to-width-down/184?cb=20150928202729")
    
        await ctx.channel.send("Hello! Here's a cool embed.", embed=embed) # Send the embed with some text


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Embed(bot)) # add the cog to the bot