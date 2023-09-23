from Classes.Class import Class
from Races.Race import Race
from Stats import Stats


class Character():
    """
    This is the root class from which Race, Stats, and Class classes should stem
    I added some basic inputs but could easily add more
    """
    def __init__(self, race: Race, class_obj: Class, stats: Stats):
        self.race = race
        self.class_obj = class_obj
        self.stats = stats  
    

