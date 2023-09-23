from DND.Races.Race import Race


class human(Race):
    def __init__(self):
        # in inches
        super().__init__("Human")
        self.height = 68

