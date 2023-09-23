class DnDCharacterClass:
    def __init__(self, class_name, hit_points, class_features, level=1):
        self.class_name = class_name
        self.hit_points = hit_points
        self.class_features = class_features
        self.level = level

    def display_class_info(self):
        print("Class Name:", self.class_name)
        print("Level:", self.level)
        print("Hit Points:", self.hit_points)
        print("Class Features:")
        for feature in self.class_features:
            print("- " + feature)

    def level_up(self):
        self.level += 1
        self.hit_points += 5  #We can use the roll function to roll more health
        print(f"{self.class_name} leveled up to level {self.level}!")
