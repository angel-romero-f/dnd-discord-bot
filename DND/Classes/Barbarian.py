from Class import Class

"""
Class for the barbarian class
"""
class Barbarian(Class):
    def __init__(self):
        super().__init__(["Strong, Heavy Armor"], "barbarian")
        self.speciality = 'Rage' 
        