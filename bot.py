import discord
from discord.ext import commands
import asyncio
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
	
asyncio.run(main())


