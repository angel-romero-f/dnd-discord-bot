from Classes.Class import Class
from Races.Race import Race
from Stats import Stats
import random 

class Character():
    """
    This is the root class from which Race, Stats, and Class classes should stem
    I added some basic inputs but could easily add more
    """
    def __init__(self, race: Race, class_obj: Class, stats: Stats):
        self.race = race
        self.class_obj = class_obj
        self.stats = stats  
    
    #attack
    #dodge
    #long_rest
    #short_rest
    def change_hp(self, amount):
        self.stats.hp_change(amount)

    def attack(self, attack: str, target):
        dmg = 0
        if attack == "armed":
            dmg = random.randint(1,8) + self.stats.get_strength()
        if attack == "unarmed":
            dmg = 0 if self.stats.get_strength() == 0 else self.stats.get_strength()
        else:
            raise Exception("Attack must be 'armed' or 'unarmed'")
        succesful = True if random.randint(1,20) > self.race.get_base_ac() else False
        if succesful:
            target.change_hp(-dmg)
            return "Your hit was a success and it did {dmg} damage!"
        else:
            return "Lol you missed"

    def long_rest(self):
        self.stats.set_hp(self.stats.get_total_hp())
        if self.class_obj.get_name == 'bard':
            self.class_obj.set_curr_slots(self.class_obj.get_max_slots())
        return "You took a long rest!"


