import random 
import discord
from discord.ext import commands
import asyncio

class DM(commands.Cog):
    def __init__(self, client):
        self.client = client