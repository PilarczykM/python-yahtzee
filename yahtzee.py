import re


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