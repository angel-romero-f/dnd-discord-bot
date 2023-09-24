from Class import Class
import random
class Bard(Class):
    """
    Constructor for the bard class, should definitely override some methods
    like level up to allow for more class specific results
    this is where attributes of this class should be held
    """
    def __init__(self):
        super().__init__(["Musical", "Armor"], "bard")
        self.speciality = 'Inspiration' 
        self.max_slots = 2
        self.curr_slots = 2
    def get_curr_slots(self):
        return self.curr_slots
    def get_max_slots(self):
        return self.max_slots
    def set_curr_slots(self, amt):
        self.curr_slots = amt
    