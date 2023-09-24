from Race import Race

class Dwarf(Race):
    def __init__(self):
        super().__init__("Dwarf")
        self.height = 41
        self.base_ac = 8
        self.resistances.append("Poison")
        self.dark_vision = True
