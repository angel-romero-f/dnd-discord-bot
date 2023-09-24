import random 
import discord
from discord.ext import commands
import asyncio
import sys
sys.path.append('DND/')
sys.path.append('DND/Classes/')
from Stats import Stats
from Classes.Bard import Bard
from Classes.Rogue import Rogue
from Classes.Barbarian import Barbarian
from Classes.Class import Class
from Character import Character
from player import Player

class DM(Player, commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(name = 'level_up',
                      brief = 'levels up a character')
    async def level_up(self, ctx: commands.Context, user):
        """
        Levels up a character and returns the new stats
        """
        character = self.character_ids[user]
        character.get_stats().level_up()
        await ctx.send(character.get_info())

async def setup(client):
    await client.add_cog(DM(client))