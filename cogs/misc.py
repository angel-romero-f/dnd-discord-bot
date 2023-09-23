import random 

def roll(n):
    """
    Rolls a n-sided dice.
    Inputs:
    n = integer representing the number of sides of the die.
    """
    return str(random.randint(1,n))