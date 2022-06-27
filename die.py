import random


class Die(object):

    def __init__(self, sides=6):
        self.sides = sides
        # Make __face private to prevent cheating
        self.__face = None

    def roll(self):
        self.__face = random.randint(1, self.sides)

    def clear(self):
        self.__face = None

    def get_face(self):
        return self.__face

    def __str__(self):
        if self.__face:
            return "Value: " + str(self.__face)
        else:
            return "Die has not been thrown"
