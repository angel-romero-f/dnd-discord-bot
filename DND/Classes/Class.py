class Class:
    """
    Inputs: 
    class_name: takes in a valid string e.g. 'Bard', 'Cleric' and holds that class information
    hit_points: an integer that represents the total health of a character
    class_features: a list any particular feats that need to be declared on construction
    level: an integer with a default value of 1 to represent the level the character is at
    """
    
    def __init__(self, profiencies, name):
        self.name = name
        self.profiiencies = profiencies




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


