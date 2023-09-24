import discord
from discord.ext import commands
import asyncio



intents = discord.Intents.all()
bot = commands.Bot(command_prefix = commands.when_mentioned_or('!'), intents = intents)

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user} (ID: {bot.user.id})')
	print('------')

async def main():




	await bot.load_extension('cogs.misc')
	await bot.load_extension('cogs.campaign')
	await bot.load_extension('cogs.chatbot')

	await bot.start('MTE1NDk5NjUyNzA3MzM0NTU4Nw.Ga9JEb.2v5fCD73nONnyg7SPXfZ9ImxkE2Yv2rRggGxGI')
	



asyncio.run(main())


