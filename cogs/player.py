import discord
from discord.ext import commands
import asyncio
import sys

sys.path.append('DND/')

from Stats import Stats
import Classes.Class as Class

class Player(commands.Cog):
    character_ids = {}

    def __init__(self, client):
        self.client = client

    @commands.command(name = 'new_char')
    async def new_char(self, ctx: commands.Context, name: str, class_name: str):
        self.character_ids[ctx.author] = name
        await ctx.send(f'hello {name}!' )
        
        class_obj = None
        stat = Stats()


        if class_name.lower() == "bard":
            class_obj = Class.Bard()
        await ctx.send(f"You choose the {class_name} class!")
        await ctx.send(f"Based on your class of choice, your stats are:")
        await ctx.send(stat.statroll(class_obj))

        

    @commands.command(name = "char_name")
    async def char_name(self, ctx: commands.Context):
        await ctx.send(self.character_ids[ctx.author])



async def setup(client):
    await client.add_cog(Player(client))