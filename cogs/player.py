import discord
from discord.ext import commands
import asyncio

class Player(commands.Cog):
    character_ids = {}

    def __init__(self, client):
        pass