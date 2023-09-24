import discord
from discord.ext import commands
import asyncio
import sys
sys.path.append('DND/')
sys.path.append('DND/Classes/')
sys.path.append('DND/Races')

from Races.Dwarf import Dwarf
from Races.Human import Human
from Races.Goblin import Goblin


from Stats import Stats
from Classes.Bard import Bard
from Classes.Rogue import Rogue
from Classes.Barbarian import Barbarian
from Character import Character

class Player(commands.Cog):
    character_ids = {}

    def __init__(self, client):
        self.client = client

    @commands.command(name = 'new_char')
    async def new_char(self, ctx: commands.Context, name: str, class_name: str, race_name: str):
        await ctx.send(f'hello {name}!' )
        class_obj = None
        race_obj = None
        stat = Stats()

        if class_name.lower() == "bard":  
            class_obj = Bard()
        elif class_name.lower() == "rogue":
            class_obj = Rogue()
        elif class_name.lower() == "barbarian":
            class_obj = Barbarian()
        
        if race_name.lower() == 'Human':
            race_obj = Human()
        elif race_name.lower() == 'Dwarf':
            race_obj = Dwarf()
        elif race_name.lower() == 'Goblin':
            race_obj = Goblin()

        await ctx.send(f"You chose the {class_name} class and the {race_name} race!")
        await ctx.send(f"Based on your class of choice, your stats are:")
        try:
            await ctx.send(stat.statroll(class_obj))
        except Exception as e:
            await ctx.send(f'{e}')
        self.character_ids[ctx.author] = Character(race_obj, class_obj, stat)
        

    

    @commands.command(name = "char_name")
    async def char_name(self, ctx: commands.Context):
        await ctx.send(self.character_ids[ctx.author])

def get_character_id(self):
    """
    Returns character_id
    """
    return self.character_ids






























    @commands.command(name = 'level_up',
                      brief = 'levels up a character')
    async def level_up(self, ctx: commands.Context, user):
        """
        Levels up a character and returns the new stats
        """
        print('here')
        try:   
            character = self.character_ids[user]
        except Exception as e:
            await ctx.send(f'e')
        print('here')

        character.get_stats().level_up()
        await ctx.send(character.get_info())

async def setup(client):
    await client.add_cog(Player(client))