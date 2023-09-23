from cogs import Character
class Class(Character):
    """
    Inputs: 
    class_name: takes in a valid string e.g. 'Bard', 'Cleric' and holds that class information
    hit_points: an integer that represents the total health of a character
    class_features: a list any particular feats that need to be declared on construction
    level: an integer with a default value of 1 to represent the level the character is at
    """
    def __init__(self, class_name, hit_points, class_features, level=1):
        super().__init__(class_name, hit_points, class_features, level)


    def display_class_info(self):
        """
        Displays the relevant information about a character when requested
        """
        print("Class Name:", self.class_name)
        print("Level:", self.level)
        print("Hit Points:", self.hit_points)
        print("Class Features:")
        for feature in self.class_features:
            print("- " + feature)

    def level_up(self):
        """
        Increases the level of a character by 1
        Notes: 
        Should be overriden in each class since this get complex real quick and are different between classes
        Should probably be a DM only function
        """
        self.level += 1
        self.hit_points += 5  #We can use the roll function to roll more health
        print(f"{self.class_name} leveled up to level {self.level}!")
