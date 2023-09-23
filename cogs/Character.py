class Character():
    def __init__(self, race, class_name, hit_points, class_features, level=1):
        self.class_name = class_name
        self.hit_points = hit_points
        self.class_features = class_features
        self.level = level
        self.race = race
    pass