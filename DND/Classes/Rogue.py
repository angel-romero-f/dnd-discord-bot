from Class import Class

"""
Class for the wizard class
"""
class Rogue(Class):
    def __init__(self):
        super().__init__(["Sleight of Hand, Thieve's Tools"], "rogue")
        self.speciality = 'Sneak Attack' 
