import re

from die import Die


class Hand(object):

    def __init__(self, dice=5, sides=6):
        self.dice = dice
        self.hand = []
        for x in range(dice):
            self.hand.append(Die(sides))

    def throw(self):
        print("\nRolling dice...")
        for die in self.hand:
            die.roll()

    def clear(self):
        for die in self.hand:
            die.clear()

    def re_roll(self):
        rolls = 0
        while rolls < 2:
            try:
                re_roll = input("\nChoose which dice to re-roll "
                                "(comma-separated or 'all'), or 0 to continue: ")

                if re_roll.lower() == "all":
                    re_roll = list(range(1, 6))
                else:
                    # Perform some clean-up of input
                    re_roll = re_roll.replace(" ", "")  # Remove spaces
                    re_roll = re.sub('[^\d,]', '', re_roll)  # Remove non-numerals
                    re_roll = re_roll.split(",")  # Turn string into list
                    re_roll = list(map(int, re_roll))  # Turn strings in list to int
            except ValueError:
                print("You entered something other than a number.")
                print("Please try again")
                continue

            if [x for x in re_roll if x > self.dice]:
                print("You only have 5 dice!")
                continue

            if not re_roll or 0 in re_roll:
                break
            else:
                for i in re_roll:
                    self.hand[i - 1].roll()
                self.show_hand()
                rolls += 1

    def get_hand(self):
        faces = []
        for face in self.hand:
            faces.append(face.get_face())
        return faces

    def show_hand(self):
        for idx, val in enumerate(self.hand):
            print("die " + str(idx + 1) + " has value " + str(val.get_face()))
