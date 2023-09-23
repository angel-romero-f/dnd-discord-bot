import discord
from discord.ext import commands
import asyncio
import sys

sys.path.append('DND/')

from Stats import Stats
from Classes.Bard import Bard
from Classes.Rogue import Rogue
from Classes.Barbarian import Barbarian

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

        if class_name == "bard":
        
            class_obj = Bard()
        elif class_name == "rogue":
            class_obj = Rogue()
        elif class_name == "barbarian":
            class_obj = Barbarian()
        

        print('here3')
        await ctx.send(f"You choose the {class_name} class!")
        print('here4')
        await ctx.send(f"Based on your class of choice, your stats are:")
        print('here5')
        await ctx.send(stat.statroll(class_obj))
        print('here6')

        

    @commands.command(name = "char_name")
    async def char_name(self, ctx: commands.Context):
        await ctx.send(self.character_ids[ctx.author])



async def setup(client):
    await client.add_cog(Player(client))