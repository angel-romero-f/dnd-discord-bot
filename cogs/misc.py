import random 
import discord
from discord.ext import commands
import asyncio

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(name = 'roll',
                      brief = 'rolls a fair n sided die')
    async def roll(self, ctx: commands.Context, num_sides: int, num_dice: int = 1, advantage: bool = False):
        """
        Rolls a n-sided dice.
        Inputs:
        num_sides = integer representing the number of sides of the die (required).
        num_dice = integer representing the number of dice rolled (optional, default is 1).
        advantage = boolean flag indicating whether it's an advantage roll (optional, default is False).
        Outputs: A dice roll that is modified by the number of dice rolled, the number of faces, and 
        whether or not we use advantage
        """
        if num_sides <= 0 or num_dice <= 0:
            await ctx.send("Please provide positive values for the number of dice and sides.")
            return

        if advantage:
            # Advantage roll - roll two dice and take the higher result
            rolls = [random.randint(1, num_sides) for _ in range(2 * num_dice)]
            results = [max(rolls[i], rolls[i + 1]) for i in range(0, len(rolls), 2)]
        else:
            # Regular roll - roll the specified number of dice
            results = [random.randint(1, num_sides) for _ in range(num_dice)]

        result_str = f'Advantage Roll: {", ".join(map(str, results))}' if advantage else f'Roll: {", ".join(map(str, results))}'
        await ctx.send(result_str)

async def setup(client):
    await client.add_cog(Misc(client))