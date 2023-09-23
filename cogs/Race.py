from cogs import Character
class Race(Character):
    """
    Contains information pertaining to each race such as:
    Proficiencies, base speed, base AC, special attacks, and any resistances
    We agreed to work on human and dwarf first
    """
    def __init__(self, race):
        super().__init__(race)