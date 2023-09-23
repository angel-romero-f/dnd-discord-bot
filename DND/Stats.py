from Character import Character
import random 
import discord
from discord.ext import commands
import asyncio

class Stats(Character):
    """
    Should initalize with the information of level, race, and class that way it knows what to make each stat and how to modify it
    Making use of methods like roll may be useful to create methods in here, should probably br able to display
    """
    def __init__(self, hit_points=4, strength=0, constitution=0, dexterity=0, wisdom=0, intelligence=0, charisma=0, char_lvl=1):
        self.health_points = hit_points
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


    def statroll(self):
        """
        Rolls four 6 sided die, drops the smallest die and takes the sum of the other three
        Inputs: None
        Outputs: A sequence of 6 integers each <= 18. The corresponding stat is next to the integer in the following order:
        Strength : int
        Dexterity : int
        Constitution : int 
        Intelligence : int 
        Wisdom : int 
        Charisma : int 
        """
        stats = [self.strength, self.constitution, self.dexterity, self.wisdom, self.intelligence, self.charisma]
        for statroll in range(7):
            stat = 0
            rolls = [random.randint(1, 6) for _ in range(5)]
            discard_roll = min(rolls)
            rolls.pop(discard_roll)
            sum_rolls = sum(rolls)
            stats[sum_rolls] = stat
        return "Strength: " + str(stats[0]) + "/n Dexterity: " + str(stats[1]) + "/n Constitution: " + str(stats[2]) + "/n Intelligence: " + str(stats[3]) + "/n Wisdom: " + str(stats[4]) + "/n Charisma: " + str(stats[5])