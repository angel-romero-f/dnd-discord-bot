import discord
from discord.ext import commands
import asyncio

from DND.Stats import Stats

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


    @commands.command(name = "stat_roll")
    async def stat_roll(self, ctx:commands.Context):
        stats = Stats()
        stat_rolls = stats.statroll()
        await ctx.send(f'Your stats are: \n {stat_rolls}')
        

async def setup(client):
    await client.add_cog(Player(client))