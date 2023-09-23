import openai
import discord
from discord.ext import commands
import asyncio

openai.api_key = "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"


class ChatBot(commands.Cog):
    def __init__(self, client):
        self.client = client
    def generate_gpt3_response(self, prompt):
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

    @commands.command(name = "talk")
    async def talk(self, ctx, message: str):

        # Use the previously set OpenAI API key
        response = self.generate_gpt3_response(message)
        print(response)
        await ctx.send(response)

    @commands.command(name = "talk_to_character")

    async def talk_to_character(self, ctx, character: str):
        # Check if the character choice is valid
        valid_characters = ['peasant', 'thief', 'merchant']
        if character.lower() not in valid_characters:
            await ctx.send("Invalid character choice. Please choose from 'peasant,' 'thief,' or 'merchant'.")
            return

        # Prompt to start the conversation with the chosen character
        prompt = f"You are talking to the {character}."

        # Generate a response from GPT-3
        response = self.generate_gpt3_response(prompt)

        # Send the response back to the user
        await ctx.send(f"{character.capitalize()}: {response}")

async def setup(client):
    await client.add_cog(ChatBot(client))