import openai
from discord.ext import commands
import asyncio

class Encounters(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='npc',
                      brief='gives players a prompt from an npc')
    async def npc(self, ctx: commands.Context):
<<<<<<< HEAD
        try:
            await ctx.send(" The party enters the kings crypt, and in front of them stands a large wall, with images of the long history of the kingdom adorning it. Noompar wishes he could enjoy it more, but he's quick to point out the large word painted in fresh blood : \n   ▄▄▄▄   ▓█████  █     █░ ▄▄▄       ██▀███  ▓█████  \n  ▓█████▄ ▓█   ▀ ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀  \n ▒██▒ ▄██▒███   ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   \n  ▒██░█▀  ▒▓█  ▄ ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ \n ░▓█  ▀█▓░▒████▒░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒ \n  ░▒▓███▀▒░░ ▒░ ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░ \n    ▒░▒   ░  ░ ░  ░  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░ \n    ░    ░    ░     ░   ░    ░   ▒     ░░   ░    ░   \n    ░         ░  ░    ░          ░  ░   ░        ░  ░ \n     ░          " )
        except Exception as e:
            await ctx.send(f'{e}')
=======
        await ctx.send(" The party enters the kings crypt, and in front of them stands a large wall, with images of the long history of the kingdom adorning it. Noompar wishes he could enjoy it more, but he's quick to point out the large word painted in fresh blood : \n ",  " ▄▄▄▄   ▓█████  █     █░ ▄▄▄       ██▀███  ▓█████  \n" ,"  ▓█████▄ ▓█   ▀ ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀  \n",  " ▒██▒ ▄██▒███   ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   \n",  "  ▒██░█▀  ▒▓█  ▄ ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ \n", " ░▓█  ▀█▓░▒████▒░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒ \n","  ░▒▓███▀▒░░ ▒░ ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░ \n","    ▒░▒   ░  ░ ░  ░  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░ \n" ,  "    ░    ░    ░     ░   ░    ░   ▒     ░░   ░    ░   \n","     ░         ░  ░    ░          ░  ░   ░        ░  ░ \n",  "     ░          " )
    @commands.command(name='kingdom',
                      brief='gives players a prompt to investigate')
    async def kingdom(self, ctx: commands.Context):
        await ctx.send(" After a tiresome journey through the forest of St. Maxine, the party stumbles upon the great kingdom of Florencia.\n                T~~      \n               |        \n              / \       \n      T~~     |'| T~~   \n T~~ |    T~ WWWW|     \n  |  / \   |  |  |/\T~~ \n / \ WWW  / \ |  |WW|   \nWWWWW/\| /   \| /\|/ \  \n|   /__\/]WWW[\/__\WWWW \n|   WWWW |I_I| WWWW   | \n|   |' |/  -  \|' |'  | \n|'  |  |LI=H=LI|' |   | \n|   |' | |[_]| |  |'  | \n|   |  |_|###|_|  |   | \n-/\—|-/___\-'--'---'  | \n ")
>>>>>>> dac4cb6124a0c9494e28535b14dc3b3191cc41ad


async def setup(client):
    await client.add_cog(Encounters(client))

