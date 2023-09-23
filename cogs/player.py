import discord
from discord.ext import commands
import asyncio


class PollButton(discord.ui.Button):
    message = ''
    count = 0

    # constructor for this poll button.
    def __init__(self, message):
        # calls the super constructor to give the label and style of the button
        super().__init__(label=message, style=discord.ButtonStyle.primary)
        self.message = message

    # defines the behavior after a user clicks a poll button (returns user choice and increments poll)
    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's choice and increment the poll
        self.count += 1
        user1 = interaction.user
        await interaction.response.send_message(f'{user1.mention}\'s choice is {self.message}', ephemeral = True)

class Player(commands.Cog):
    character_ids = {}

    def __init__(self, client):
        self.client = client

    @commands.command(name = 'new_char')
    async def new_char(self, ctx: commands.Context, name):
        self.character_ids[ctx.author] = name
        await ctx.send(f'hello {name}!' )

    @commands.command(name = "char_name")
    async def char_name(self, ctx: commands.Context):
        await ctx.send(self.character_ids[ctx.author])

    

async def setup(client):
    await client.add_cog(Player(client))