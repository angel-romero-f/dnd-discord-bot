from Classes.Class import Class
from Races.Race import Race
from Stats import Stats
import random 

class Character():
    """
    This is the root class from which Race, Stats, and Class classes should stem
    I added some basic inputs but could easily add more
    """
    def __init__(self, race: Race, class_obj: Class, stats: Stats, name: str):
        '''
        Initializes a character with all the needed values
        '''
        self.race = race
        self.class_obj = class_obj
        self.stats = stats      
        self.name = name
    
    #attack
    #dodge
    #long_rest
    #short_rest

    def attackc(self, attack: str, target):
        '''
        Represents a character attack, uses attacks that a character can do to modify the health of another
        character
        '''
        dmg = 0
        if attack == "armed":
            dmg = random.randint(1,8) + self.stats.get_strength() // 3 
        if attack == "unarmed":
            dmg = 0 if self.stats.get_strength() == 0 else self.stats.get_strength() // 3
        succesful = True if random.randint(1,20) > target.race.get_base_ac() else False
        if succesful:
            target.get_stats().hp_change(-dmg)
            return f"Your hit was a success and it did {dmg} damage!"
        else:
            return "Lol you missed"

    def long_rest(self):
        '''
        Resets health points and spell slots to their max val
        Inputs: a character obj
        Outputs: void
        '''
        self.stats.set_hp(self.stats.get_total_hp())
        if self.class_obj.get_name() == 'bard':
            self.class_obj.set_curr_slots(self.class_obj.get_max_slots())
        return "You took a long rest!"
    def get_stats(self):
        return self.stats
    
    def get_info(self):
        line1 = self.class_obj.display_class_info()
        line2 = "Strength: {stats[0]}\nDexterity: {stats[1]}\nConstitution: {stats[2]}\nWisdom: {stats[3]}\nIntelligence: {stats[4]}\nCharisma: {stats[5]}\nHP: {stats[-1]}"
        return f'{line1}\n+{line2}'
    
    def get_class(self):
        return self.class_obj
    def get_race(self):
        return self.race
    def get_name(self):
        return self.name
    def check_death(self):
        return self.stats.get_hp <= 0
    


