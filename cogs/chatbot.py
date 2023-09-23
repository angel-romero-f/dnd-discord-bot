import openai
from discord.ext import commands
import asyncio


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    openai_key = "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"
    def generate_gpt3_response(prompt):
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n = 1,
        stop=None
    )
        return response.choices[0].text

    response = generate_gpt3_response(message.content)

    await message.channel.send(response)

bot.run('YOUR_BOT_TOKEN')
