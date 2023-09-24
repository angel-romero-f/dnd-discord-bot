import openai
from discord.ext import commands
import asyncio

class Encounters(commands.Cog):
    def __init__(self, client):
        self.client
    
    @commands.command(name='npc',
                      brief='gives players a prompt from an npc')
    async def npc(self, ctx: commands.Context):
        await ctx.send(" The party enters the kings crypt, and in front of them stands a large wall, with images of the long history of the kingdom adorning it. Noompar wishes he could enjoy it more, but he's quick to point out the large word painted in fresh blood : \n ",  " ▄▄▄▄   ▓█████  █     █░ ▄▄▄       ██▀███  ▓█████  \n" ,"  ▓█████▄ ▓█   ▀ ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀  \n",  " ▒██▒ ▄██▒███   ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   \n",  "  ▒██░█▀  ▒▓█  ▄ ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ \n", " ░▓█  ▀█▓░▒████▒░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒ \n","  ░▒▓███▀▒░░ ▒░ ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░ \n","    ▒░▒   ░  ░ ░  ░  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░ \n" ,  "    ░    ░    ░     ░   ░    ░   ▒     ░░   ░    ░   \n","     ░         ░  ░    ░          ░  ░   ░        ░  ░ \n",  "     ░          " )



async def setup(client):
    await client.add_cog(Encounters(client))

