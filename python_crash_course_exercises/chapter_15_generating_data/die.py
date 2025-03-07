from random import randint


class Die():
    """ A class representing a single die."""

    def __init__(self, num_sides=6):
        """ Assume a die has 6 sides."""
        self.num_sides = num_sides

    def roll(self):
        """ Returns a random value between 1 and num_sides."""
        return randint(1, self.num_sides)
