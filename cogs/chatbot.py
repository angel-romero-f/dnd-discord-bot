import openai
import discord
from discord.ext import commands
import asyncio

openai.api_key = "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"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = commands.when_mentioned_or('!'), intents = intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def generate_gpt3_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None
        )
        return response.choices[0].text
    except Exception as e:
        # Handle any exceptions here (e.g., print an error message)
        print(f"Error generating GPT-3 response: {e}")
        return "An error occurred while generating the response."

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Use the previously set OpenAI API key
    response = generate_gpt3_response(message.content)

    await message.channel.send(response)

async def talk_to_character(ctx, character: str):
    # Check if the character choice is valid
    valid_characters = ['peasant', 'thief', 'merchant']
    if character.lower() not in valid_characters:
        await ctx.send("Invalid character choice. Please choose from 'peasant,' 'thief,' or 'merchant'.")
        return

    # Prompt to start the conversation with the chosen character
    prompt = f"You are talking to the {character}."

    # Generate a response from GPT-3
    response = generate_gpt3_response(prompt)

    # Send the response back to the user
    await ctx.send(f"{character.capitalize()}: {response}")

bot.run('MTE1NDk5NjUyNzA3MzM0NTU4Nw.Ga9JEb.2v5fCD73nONnyg7SPXfZ9ImxkE2Yv2rRggGxGI')