import random 
import discord
from discord.ext import commands
import asyncio


@commands.command(name = 'roll',
                  brief = 'roll an n sided dice')

async def roll(ctx: commands.Context, num_sides: int):
    """
    Rolls a n-sided dice.
    Inputs:
    n = integer representing the number of sides of the die.
    """
    await ctx.send(f"You rolled {random.randrange(1,num_sides + 1)}")
