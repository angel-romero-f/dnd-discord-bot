from DND.Character import Character


class Spell:
    """
    This class should contain a few spells and their functions like cast and heal
    This is where spell information should go
    """
    def get_Description(name):
        '''
        Returns a brief description of spells
        '''
        if name.lower() == "fire bolt":
            return "You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn’t being worn or carried. This spell’s damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10)."
        if name.lower() == "cure wounds":
            return "A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs. At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, the Healing increases by 1d8 for each slot level above 1st."
        if name.lower() == "create water" or name.lower() == "destroy water" or name.lower() == "create or destroy water":
            return "You either create or destroy water. Create Water. You create up to 10 gallons of clean water within range in an open container. Alternatively, the water falls as rain in a 30-foot cube within range, extinguishing exposed flames in the area. Destroy Water. You destroy up to 10 gallons of water in an open container within range. Alternatively, you destroy fog in a 30-foot cube within range. At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, you create or destroy 10 additional gallons of water, or the size of the cube increases by 5 feet, for each slot level above 1st."
        else:
            return "Invalid spell name"
    
    def cast(spell, target):
        '''
        Method to make the spell have an affect
        '''
        if spell.lower() == "fire bolt":
            pass
        if spell.lower() == "cure wounds":
            pass
        if spell.lower() == "create water" or spell.lower() == "destroy water" or spell.lower() == "create or destroy water":
            pass
        