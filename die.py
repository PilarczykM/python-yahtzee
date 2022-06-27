import random


class Die():
    def __init__(self, sides=6, face: int = None):
        self.sides = sides
        if face is not None:
            self.__face = face
        else:
            self.roll()

    def roll(self):
        self.__face = random.randint(1, self.sides)

    def get_face(self):
        return self.__face

    def set_face(self, face):
        self.__face = face

    def __str__(self):
        return str(self.__face)
