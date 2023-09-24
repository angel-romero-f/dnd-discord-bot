from DND.Races.Race import Race
class Goblin(Race):
    def __init__(self):
        super().__init__("Dwarf")
        self.height = 30
        self.base_ac = 6
        self.dark_vision = True