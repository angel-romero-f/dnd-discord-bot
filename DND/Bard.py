from Class import Class
import random
class Bard(Class):
    """
    Constructor for the bard class, should definitely override some methods
    like level up to allow for more class specific results
    this is where attributes of this class should be held
    """
    def __init__(self, class_name, hit_points, class_features, slots, level=1, instrument=None):
        super().__init__(class_name, hit_points, class_features, level)
        self.instrument = instrument
        self.slots = slots
    
    def alter_slots(self, level, change):
        a = self.slots[level]
        self.slots[level] = a+change

    def inspire(self, target):
        if self.level < 5:
            add = random.randint(1, 7)
            target.mod += add
        elif self.level < 10:
            add = random.randint(1, 9)
            target.mod += add
        elif self.level < 15:
            add = random.randint(1, 11)
            target.mod += add
        else:
            add = random.randint(1, 13)
            target.mod += add

    
