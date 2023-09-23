from cogs import Character
class Stats(Character):
    """
    Should initalize with the information of level, race, and class that way it knows what to make each stat and how to modify it
    Making use of methods like roll may be useful to create methods in here, should probably br able to display
    """
    def __init__(self, hit_points, strength, cons, dext, wis, intelligence, charisma, char_lvl):
        self.health_points = hit_points
        self.strength = strength 
        self.cons = cons
        self.dext = dext
        self.wis = wis
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

    def hp_change(self):
        """
        How the hp of the characters evolves throughout the game. Independent of the total hitpoints. 
        """
                