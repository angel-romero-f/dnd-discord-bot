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

async def main():
	try:
		await bot.load_extension("cogs.rps")
		await bot.load_extension("cogs.util")
		print(f'Extension loaded!')
	except Exception as e:
		print(f'Failed to load extension cogs.')
		print(str(e))
	await bot.start('MTE1NDk5NjUyNzA3MzM0NTU4Nw.Ga9JEb.2v5fCD73nONnyg7SPXfZ9ImxkE2Yv2rRggGxGI')
	
asyncio.run(main())


