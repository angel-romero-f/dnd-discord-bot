import random 
import discord
from discord.ext import commands
import asyncio

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(name = 'roll',
                      brief = 'rolls a fair n sided die')
    async def roll(self, ctx: commands.Context, num_sides: int):
        """
        Rolls a n-sided dice.
        Inputs:
        n = integer representing the number of sides of the die.
        """
        await ctx.send(f"You rolled a {random.randrange(1,num_sides + 1)}")

async def setup(client):
    await client.add_cog(Misc(client))