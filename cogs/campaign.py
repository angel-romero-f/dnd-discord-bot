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

class Campaign(commands.Cog):
    character_ids = dict()
    party = []
    enemies = []
    campaign_name = ''
    campaign = False

    def __init__(self, client):
        self.client = client

    @commands.command(name = 'start_campaign')
    async def start_campaign(self, ctx: commands.Context, name: str):
        """
        Starts a new campaign
        """
        roles = ctx.author.roles

        if self.campaign:
                await ctx.send("There is already a campaign in progress!")
                return
        if "DM" in list(map(lambda role: role.name, roles)):
            self.campaign_name = name
            self.campaign = True
            await ctx.send(f'The group is off on their adventure of {name}!')
        else:
            await ctx.send("You're not authorized to use this command bozo!!")

    @commands.command(name = 'campaign_info')
    async def campaign_info(self, ctx: commands.Context):
        """
        Starts a new campaign
        """
        await ctx.send(f'Campaign name: {self.campaign_name}\nParty members: {self.party}')

    @commands.command(name = 'new_char')
    async def new_char(self, ctx: commands.Context, name: str, class_name: str, race_name: str, enemy = False):


        class_obj = None
        race_obj = None
        stat = Stats()

        if class_name.lower() == "bard":  
            class_obj = Bard()
        elif class_name.lower() == "rogue":
            class_obj = Rogue()
        elif class_name.lower() == "barbarian":
            class_obj = Barbarian()
        
        if race_name.lower() == 'human':
            race_obj = Human()
        elif race_name.lower() == 'dwarf':
            race_obj = Dwarf()
        elif race_name.lower() == 'goblin':
            race_obj = Goblin()
        if not enemy:
            await ctx.send(f'hello {name}!' )
            await ctx.send(f"You chose the {class_name} class and the {race_name} race!")
            await ctx.send(f"Based on your class of choice, your stats are:")
            await ctx.send(stat.statroll(class_obj))
        else:
            await ctx.send("Succesfully created an enemy.")
            stat.statroll(class_obj)

        char = Character(race_obj, class_obj, stat, name)
        self.character_ids[ctx.author] = char
        if enemy:
            self.enemies.append(char)
        self.party.append(char)

    

    @commands.command(name = "char_name")
    async def char_name(self, ctx: commands.Context):
        await ctx.send(self.character_ids[ctx.author].get_name())
    
    @commands.command(name = "player_info")
    async def player_info(self, ctx: commands.Context):
        """
        Returns player class, race, and health in the form:
        Player name: str
        Class: str
        Race: str
        Current_hp: str
        """
        try:
            await ctx.send(f"Character name: {self.character_ids[ctx.author].get_name()} \nClass: {self.character_ids[ctx.author].get_class().get_name()} \nRace: {self.character_ids[ctx.author].get_race().get_name()} \nCurrent Hit Points: {self.character_ids[ctx.author].get_stats().get_hp()}")
        except Exception as e:
            await ctx.send(f'{e}')
            
    @commands.command(name = 'list_enemies')
    async def list_enemies(self,ctx: commands.Context):
        await ctx.send(f"Here's a list of the current enemies.")
        for idx, enemy in enumerate(self.enemies):
            
            await ctx.send(f'{idx} - {enemy.get_name()}' )
    @commands.command(name = 'attack')
    async def attack(self, ctx: commands.Context, enemy: int, type : str):
        if type != "armed" and type != "unarmed":
            await ctx.send("attack must be 'armed' or 'unarmed' ")
            return
        if not(enemy >= 0 and enemy < len(self.enemies)):
            await ctx.send("must choose a valid enemy to attack!")
            return
        await ctx.send(f"{self.character_ids[ctx.author].get_name()} is attempting an {type} attack against {self.enemies[enemy].get_name()}.")

        try:
            msg = self.character_ids[ctx.author].attackc(type, self.enemies[enemy])
            await ctx.send(msg)
        except Exception as e:
            print(e)
            await ctx.send(f'lol doesnt work {e}')

        if self.enemies[enemy].check_death():
            await ctx.send(f"{self.character_ids[ctx.author].get_name()} has defeated {self.enemies[enemy].get_name()}")
            self.enemies.remove(enemy)
        


async def setup(client):
    await client.add_cog(Campaign(client))