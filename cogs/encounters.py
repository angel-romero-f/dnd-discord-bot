import openai
from discord.ext import commands
import asyncio

class Encounters(commands.Cog):
    def __init__(self, client):
        self.client
    
    @commands.command(name='npc',
                      brief='gives players a prompt from an npc')
    async def npc(self, ctx: commands.Context):
        await ctx.send(' 
▄▄▄▄   ▓█████  █     █░ ▄▄▄       ██▀███  ▓█████ 
▓█████▄ ▓█   ▀ ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀ 
▒██▒ ▄██▒███   ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   
▒██░█▀  ▒▓█  ▄ ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ 
░▓█  ▀█▓░▒████▒░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒
░▒▓███▀▒░░ ▒░ ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░
▒░▒   ░  ░ ░  ░  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░
 ░    ░    ░     ░   ░    ░   ▒     ░░   ░    ░   
 ░         ░  ░    ░          ░  ░   ░        ░  ░
      ░                                           ')



async def setup(client):
    await client.add_cog(Encounters(client))

