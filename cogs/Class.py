class DnDCharacterClass:
    def __init__(self, class_name, hit_points, class_features):
        self.class_name = class_name
        self.hit_points = hit_points
        self.class_features = class_features

    def display_class_info(self):
        print("Class Name:", self.class_name)
        print("Hit Points:", self.hit_points)
        print("Class Features:")
        for feature in self.class_features:
            print("- " + feature)
