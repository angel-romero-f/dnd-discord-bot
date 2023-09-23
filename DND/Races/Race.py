class Race:
    """
    Contains information pertaining to each race such as:
    Proficiencies, base speed, base AC, special attacks, and any resistances
    We agreed to work on human and dwarf first
    """
    base_speed = 0
    base_ac = 0
    resistances = []
    traits = []
    height = 0
    def __init__(self, race_name):
        self.race = race_name

    
    def get_speed(self):
        """
        returns base speed for this race
        """
        return self.base_speed
    def get_ac(self):
        """
        returns base AC for this race
        """
        return self.base_ac
    def get_resistances(self):
        """
        returns the resistances associated with this race
        """
        return self.resistances
    def get_traits(self):
        """
        returns the traits associated with this race
        """
        return self.traits