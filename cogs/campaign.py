import discord
from discord.ext import commands
import asyncio
import sys
sys.path.append('DND/')
sys.path.append('DND/Classes/')
sys.path.append('DND/Races')
sys.path.append('DND/Spell.py')

from Spell import Spell
from Races.Dwarf import Dwarf
from Races.Human import Human
from Races.Goblin import Goblin


from Stats import Stats
from Classes.Bard import Bard
from Classes.Rogue import Rogue
from Classes.Barbarian import Barbarian
from Character import Character

class Campaign(Spell, commands.Cog):
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

    @commands.command(name = 'level_up')
    async def level_up(self, ctx: commands.Context, name: str):
        roles = ctx.author.roles
        if "DM" in list(map(lambda role: role.name, roles)):  
            await ctx.send(self.character_ids[name].get_stats().level_up(self.character_ids[name].get_class()))
            await ctx.send(f"Your current stats are...\nStrength: {self.character_ids[name].get_stats().get_strength()} \nDexterity: {self.character_ids[name].get_stats().get_dexterity()} \nConstitution: {self.character_ids[name].get_stats().get_constitution()} \nWisdom: {self.character_ids[name].get_stats().get_wisdom()} \nIntelligence: {self.character_ids[name].get_stats().get_intelligence()} \nCharisma: {self.character_ids[name].get_stats().get_charisma()} \nCurrent Level: {self.character_ids[name].get_stats().get_lvl()} \nHP: {self.character_ids[name].get_stats().get_hp()}")
        else:
            await ctx.send("You are not authorized to use this command.")

    @commands.command(name = 'spellbook')
    async def spellbook(self, ctx : commands.Context):
        """
        Returns a list of spells and their descriptions. 
        """
        await ctx.send(f"Fire Bolt: You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn’t being worn or carried. This spell’s damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10). \nCure Wounds: A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs. At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, the Healing increases by 1d8 for each slot level above 1st.\nCreate Water: You either create or destroy water. Create Water. You create up to 10 gallons of clean water within range in an open container. Alternatively, the water falls as rain in a 30-foot cube within range, extinguishing exposed flames in the area. Destroy Water. You destroy up to 10 gallons of water in an open container within range. Alternatively, you destroy fog in a 30-foot cube within range. At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, you create or destroy 10 additional gallons of water, or the size of the cube increases by 5 feet, for each slot level above 1st.")

    @commands.command(name = 'cast')
    async def cast(self, ctx: commands.Context, spell, target):  
        valid_spells = ['create or destroy water', 'firebolt', 'cure wounds']  
        vaild_target1 = self.party
        vaild_target2 = self.enemy
        if spell in valid_spells:
            if target in vaild_target1 or target in vaild_target2:
                Spell.cast(spell, target)
                await ctx.send(f'Your spell: {spell} has been cast\nYour oppenent is looking a little hurt')
        else:
            await ctx.send(f'I don\'t think you can cast that')

    @commands.command(name = 'campaign_info')
    async def campaign_info(self, ctx: commands.Context):
        """
        Starts a new campaign
        """
        await ctx.send(f'Campaign name: {self.campaign_name}\nParty members: {self.party}')

    @commands.command(name = 'new_char')
    async def new_char(self, ctx: commands.Context, name: str, class_name: str, race_name: str, enemy = False):
        if not self.campaign:
            await ctx.send("There is no current campaign to make a character for!")
            return

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
        self.character_ids[ctx.author.name] = char
        if enemy:
            self.enemies.append(char)
        else:
            self.party.append(char)
        print(self.character_ids)

    

    @commands.command(name = "char_name")
    async def char_name(self, ctx: commands.Context):
        await ctx.send(self.character_ids[ctx.author.name].get_name())
    
    @commands.command(name = "stats")
    async def stats(self, ctx: commands.Context):
        """
        Returns player stats and current level. Of the form:
        Strength: int
        Dexterity: int
        Constitution: int
        Intelligence: int
        Wisdom: int
        Charisma: int
        Level: int
        """
        await ctx.send(f"Your current stats are...\nStrength: {self.character_ids[ctx.author.name].get_stats().get_strength()} \n Dexterity: {self.character_ids[ctx.author.name].get_stats().get_dexterity()} \n Constitution: {self.character_ids[ctx.author.name].get_stats().get_constitution()} \n Wisdom: {self.character_ids[ctx.author.name].get_stats().get_wisdom()} \n Intelligence: {self.character_ids[ctx.author.name].get_stats().get_intelligence()} \n Charisma: {self.character_ids[ctx.author.name].get_stats().get_charisma()} \n Current Level: {self.character_ids[ctx.author.name].get_stats().get_lvl()} \n Health Points: {self.character_ids[ctx.author.name].get_stats().get_hp()}")

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
            await ctx.send(f"Character name: {self.character_ids[ctx.author.name].get_name()}\nClass: {self.character_ids[ctx.author.name].get_class().get_name()}\nRace: {self.character_ids[ctx.author.name].get_race().get_name()}\nCurrent Hit Points: {self.character_ids[ctx.author.name].get_stats().get_hp()}")
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
        await ctx.send(f"{self.character_ids[ctx.author.name].get_name()} is attempting an {type} attack against {self.enemies[enemy].get_name()}.")


        msg = self.character_ids[ctx.author.name].attackc(type, self.enemies[enemy])
        await ctx.send(msg)


        try:
            if self.enemies[enemy].check_death():
                await ctx.send(f"{self.character_ids[ctx.author.name].get_name()} has defeated {self.enemies[enemy].get_name()}")
                self.enemies.pop(enemy)
        except Exception as e:
            await ctx.send(f'{e}')

    @commands.command(name = 'list_party')
    async def list_party(self,ctx: commands.Context):
        await ctx.send(f"Here's a list of the current party.")
        for idx, enemy in enumerate(self.party):
            
            await ctx.send(f'{idx} - {enemy.get_name()}' )

    @commands.command(name = 'enemy_attack')
    async def enemy_attack(self, ctx: commands.Context, enemy: int, sel : int, type: str):
        if not "DM" in list(map(lambda role: role.name, ctx.author.roles)):
            ctx.send("You must be a DM to do this!")
            return

        if type != "armed" and type != "unarmed":
            await ctx.send("attack must be 'armed' or 'unarmed' ")
            return
        if not(enemy >= 0 and enemy < len(self.party)):
            await ctx.send("must choose a valid enemy to attack!")
            return
        await ctx.send(f"{self.enemies[sel].get_name()} is attempting an {type} attack against {self.party[enemy].get_name()}.")


        msg = self.enemies[sel].attackc(type, self.party[enemy])
        await ctx.send(msg)


        try:
            if self.party[enemy].check_death():
                await ctx.send(f"{self.enemies[sel].get_name()} has defeated {self.party[enemy].get_name()}")
                self.party.pop(enemy)
        except Exception as e:
            await ctx.send(f'{e}')

    @commands.command(name = "helper")
    async def help(self, ctx: commands.Context, funct):
        if funct.lower() == 'start_campaign':
            await ctx.send(f'This command requires no further inputs and starts a campaign')
        elif funct.lower() == 'level_up':
            await ctx.send(f'This function takes in the id of a player and levels up their character and increases their stats')
        elif funct.lower() == 'campaign_info':
            await ctx.send(f'This command requires no further inputs and gives the name of the campaign and the list of current party members')
        elif funct.lower() == 'new_char':
            await ctx.send('Once the DM has started a campaign, this function takes name, the name of the character, class_name, the class you want to be, race_name, the race you want to be, and whether or not you are an enemy, his is preset to be false')
        elif funct.lower() == 'char_name': 
            await ctx.send('This function requires no further input and returns the name or your current character in the campaign')
        elif funct.lower() == 'stats': 
            await ctx.send('This command requires no further input and returns player stats and current level. Of the form:\nStrength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, Level: int')
        elif funct.lower() == 'player_info': 
            await ctx.send('This command requires no further input and returns player class, race, and health')
        elif funct.lower() == 'list_enemies': 
            await ctx.send(f'This command requires no further inputs and returns a list of all current ememies')
        elif funct.lower() == 'attack': 
            await ctx.send(f'This command takes in enemy: int an integer representing an enemy, type : str you want to say it is either an \'armed\' or \'unarmed\' strike')
        elif funct.lower() == 'list_party': 
            await ctx.send(f'This command requires no further inputs and returns a list of all current party members')
        elif funct.lower() == 'cast': 
            await ctx.send(f'This command requires no further inputs and return')
        elif funct.lower() == 'enemy_attack': 
            await ctx.send(f'This command takes in enemy: int an integer representing a party member, the sel : int an integer representing the enemy you want to have attack, type: str you want to say it is either an \'armed\' or \'unarmed\' strike')
        elif funct.lower() == 'spellbook': 
            await ctx.send(f'This command requires no further inputs and returns all spells and their descriptions')
        else:
            await ctx.send(f"I don't know what to help you with")
    @commands.command(name = "funct_list")
    async def funct_list(self, ctx: commands.Context):
        await ctx.send(f'start_campaign\nlevel_up\ncampaign_info\nnew_char\nchar_name\nstats\nplayer_info\nlist_enemies\nattack\nlist_party\ncast\nenemy_attack\nspellbook')
async def setup(client):
    await client.add_cog(Campaign(client))