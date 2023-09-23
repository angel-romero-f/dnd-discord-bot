from Character import Character
from Classes.Class import Class
import Classes.Class
import random 
import discord 
from discord.ext import commands
import asyncio




class Stats(Character, Class):
    """
    Should initalize with the information of level, race, and class that way it knows what to make each stat and how to modify it
    Making use of methods like roll may be useful to create methods in here, should probably br able to display
    """
    def __init__(self, hit_points=4, strength=0, constitution=0, dexterity=0, wisdom=0, intelligence=0, charisma=0, char_lvl=1):
        self.hit_points = hit_points
        self.strength = strength 
        self.constitution = constitution
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.char_lvl = char_lvl
        self.current_hp = hit_points
    
    def level_up(self):
        """
        Increases the level of a character by 1
        Notes: 
        Should be overriden in each class since this get complex real quick and are different between classes
        Should probably be a DM only function
        """
        self.char_lvl += 1
        self.hit_points += 5  #We can use the roll function to roll more health
        self.current_hp += 5 
        print(f"{self.class_name} leveled up to level {self.char_lvl}!")

    def hp_change(self, amount):
        """
        How the hp of the characters evolves throughout the game. Independent of the total hitpoints. 
        """
        current_hp = current_hp + amount


    def statroll(self, class_obj):
        """
        Rolls four 6 sided die, drops the smallest die and takes the sum of the other three
        Inputs: class_obj = class object 
        Outputs: A sequence of 6 integers each <= 18. The corresponding stat is next to the integer in the following order:
        Strength : int
        Dexterity : int
        Constitution : int 
        Intelligence : int 
        Wisdom : int 
        Charisma : int 
        """
        stats = [self.strength, self.constitution, self.dexterity, self.wisdom, self.intelligence, self.charisma, self.hit_points]
        #rolls 4 die and discards the lowest dice. Sums the remaining die and tethers it to the corresponding stat
        for statroll in range(6):
            rolls = [random.randint(1, 6) for _ in range(4)]
            discard_roll = rolls.index(min(rolls))
            rolls.pop(discard_roll)
            sum_rolls = sum(rolls)
            stats[statroll] = sum_rolls
        #to initialize hp for given classes. determines constitution modifier based on constitution
        const_mod = 0
        if stats[1] < 10:
            if (7 < stats[1] <= 9):
                const_mod = -1 
            elif (5 < stats[1] <= 7):
                const_mod = -2
            elif (3 < stats[1] <= 5):
                const_mod = -3 
            else:
                const_mod = -4
        elif stats[1] > 10:
            if (11 <= stats[1] < 13):
                const_mod = 1
            elif (13 <= stats[1] < 15):
                const_mod = 2
            elif (15 <= stats[1] < 17):
                const_mod = 3
            else:
                const_mod = 4
        #adds constitution modifier to base hp depending on class input by user
        else:
            const_mod = 0
        if (class_obj.get_name().lower() == "wizard"):
            stats[-1] = 4 + const_mod
        elif (class_obj.get_name().lower() == "barbarian"):
            stats[-1] = 12 + const_mod
        elif (class_obj.get_name().lower() == "bard"):
            stats[-1] = 8 + const_mod
        return f"Strength: {stats[0]}\nDexterity: {stats[1]}\nConstitution: {stats[2]}\nIntelligence: {stats[3]}\nWisdom: {stats[4]}\nCharisma: {stats[5]}\nHP: {stats[-1]}"

