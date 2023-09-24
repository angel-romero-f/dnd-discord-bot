from Classes.Class import Class

import random 


class Stats(Class):
    """
    Should initalize with the information of level, race, and class that way it knows what to make each stat and how to modify it
    Making use of methods like roll may be useful to create methods in here, should probably br able to display
    """
    const_mod = 0
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
    
    def get_total_hp(self):
        """
        Returns the total hp of the character.
        """
        return self.hit_points
    
    def get_hp(self):
        """
        Returns the current healthpoints of the character.
        """
        return self.current_hp
    
    def get_strength(self):
        """
        Returns the strength of the character
        """
        return self.strength

    def get_constitution(self):
        """
        Returns the constitution of the character.
        """
        return self.constitution

    def get_dexterity(self):
        """
        Returns the dexterity of the character.
        """
        return self.dexterity

    def get_wisdom(self):
        """
        Returns the wisdom of the character.
        """
        return self.wisdom
    
    def get_intelligence(self):
        """
        Returns the intelligence of the character.
        """
        return self.intelligence
    
    def get_charisma(self):
        """
        Returns the charisma of the character.
        """
        return self.charisma
    
    def increase_strength(self, val):
        """
        Increases strength to input value. 
        """
        self.strength += val

    def increase_constitution(self, val):
        """
        Increases constitution to input value. 
        """
        self.constitution += val
    
    def increase_dexterity(self, val):
        """
        Increases dexterity to input value. 
        """
        self.dexterity += val

    def increase_wisdom(self, val):
        """
        Increases wisdom to input value. 
        """
        self.wisdom += val
    
    def increase_intelligence(self, val):
        """
        Increases charisma to intelligence value. 
        """
        self.intelligence += val

    def increase_charisma(self, val):
        """
        Increases charisma to input value. 
        """
        self.charisma += val

    def increase_level(self, val):
        """
        Increases level to input value. 
        """
        self.level += val

    def set_hp(self, val):
        """
        Set hp to input value. 
        """
        self.hp = val
        
    def roll(self, n, k):
        """
        Rolls k amount n-sided die. Can be used for health addition when leveling up. 
        Inputs: n = integer representing the number of sides on the die
        Outputs: integer representing the number on the die
        """
        die = [random.randint(1, n) for _ in range(k)]
        return sum(die)
    
    def level_up(self, class_obj):
        """
        Increases the level of a character by 1. Increases hp by a die roll corresponding to player class.
        Inputs: class_obj = class object
        Barbarian: d12
        Rogue: d8 
        Bard: d8
        Notes: 
        Should be overriden in each class since this get complex real quick and are different between classes
        Should probably be a DM only function
        """
        self.char_lvl += 1
        if (class_obj.get_name() == "rogue"):
            added_health = Stats.roll(8, 1) + self.const_mod
            self.hit_points += added_health
            self.current_hp += added_health
        elif (class_obj.get_name() == "barbarian"):
            added_health = Stats.roll(12, 1) + self.const_mod
            self.hit_points += added_health
            self.current_hp += added_health
        elif (class_obj.get_name() == "bard"):
            added_health = Stats.roll(8, 1) + self.const_mod
            self.hit_points += added_health
            self.current_hp += added_health
        print(f"{self.class_name} leveled up to level {self.char_lvl}!")
    
    def get_lvl(self):
        """
        Returns the level of the character.
        """
        return self.char_lvl

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
        stats = [self.strength, self.dexterity, self.constitution, self.wisdom, self.intelligence, self.charisma, self.hit_points]
        #rolls 4 die and discards the lowest dice. Sums the remaining die and tethers it to the corresponding stat
        for statroll in range(6):
            rolls = [random.randint(1, 6) for _ in range(4)]
            discard_roll = rolls.index(min(rolls))
            rolls.pop(discard_roll)
            sum_rolls = sum(rolls)
            stats[statroll] = sum_rolls
        #to initialize hp for given classes. determines constitution modifier based on constitution
        self.const_mod = 0
        if stats[2] < 10:
            if (7 < stats[2] <= 9):
                self.const_mod = -1 
            elif (5 < stats[2] <= 7):
                self.const_mod = -2
            elif (3 < stats[2] <= 5):
                self.const_mod = -3 
            else:
                self.const_mod = -4
        elif stats[2] > 10:
            if (11 <= stats[2] < 13):
                self.const_mod = 1
            elif (13 <= stats[2] < 15):
                self.const_mod = 2
            elif (15 <= stats[2] < 17):
                self.const_mod = 3
            else:
                self.const_mod = 4
        #adds constitution modifier to base hp depending on class input by user
        else:
            self.const_mod = 0
        if (class_obj.get_name() == "rogue"):
            stats[-1] = 6 + self.const_mod
        elif (class_obj.get_name() == "barbarian"):
            stats[-1] = 12 + self.const_mod
        elif (class_obj.get_name() == "bard"):
            stats[-1] = 8 + self.const_mod
        return f"Strength: {stats[0]}\nDexterity: {stats[1]}\nConstitution: {stats[2]}\nWisdom: {stats[3]}\nIntelligence: {stats[4]}\nCharisma: {stats[5]}\nHP: {stats[-1]}"

