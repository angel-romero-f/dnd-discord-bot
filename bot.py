import discord
from discord.ext import commands
import asyncio
import random
import cogs.misc

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = commands.when_mentioned_or('!'), intents = intents)

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user} (ID: {bot.user.id})')
	print('------')

@bot.event
async def on_message(message):
    if message.author != bot.user:
    	if message.content.startswith('!roll'):
        	# Process the roll command
        	await message.channel.send("Rolling the dice...")

async def main():
	await bot.start('MTE1NDk5NjUyNzA3MzM0NTU4Nw.Ga9JEb.2v5fCD73nONnyg7SPXfZ9ImxkE2Yv2rRggGxGI')

@bot.command()
async def roll(ctx: commands.Context):
    """
    Rolls a n-sided dice.
    Inputs:
    n = integer representing the number of sides of the die.
    """
    await ctx.send(f"You rolled {random.randrange(1,6)}")

asyncio.run(main())


