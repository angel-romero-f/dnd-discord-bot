class Character():
    """
    This is the root class from which Race, Stats, and Class classes should stem
    I added some basic inputs but could easily add more
    """
    def __init__(self, race, class_name, hit_points, class_features, level=1):
        self.class_name = class_name
        self.hit_points = hit_points
        self.class_features = class_features
        self.level = level
        self.race = race