from cogs import Class
class Bard(Class):
    def __init__(self, class_name, hit_points, class_features, level=1, instrument=None):
        super().__init__(class_name, hit_points, class_features, level)
        self.instrument = instrument
