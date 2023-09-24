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