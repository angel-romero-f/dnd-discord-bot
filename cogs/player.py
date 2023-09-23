import discord
from discord.ext import commands
import asyncio
import sys

sys.path.append('dnd-discord-bot/DND/')

from Stats import Stats

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