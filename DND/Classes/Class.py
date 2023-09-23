class Class:
    """
    Inputs: 
    class_name: takes in a valid string e.g. 'Bard', 'Cleric' and holds that class information
    hit_points: an integer that represents the total health of a character
    class_features: a list any particular feats that need to be declared on construction
    level: an integer with a default value of 1 to represent the level the character is at
    """
    
    def __init__(self, profiencies, name):
        self.class_name = name
        self.profiencies = profiencies




    def display_class_info(self):
        """
        Displays the relevant information about a character when requested
        """
        return f"Class Name: {self.class_name}\nClass Features: {repr(self.profiencies)}"
    def get_name(self):
        return self.class_name


