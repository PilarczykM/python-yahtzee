from hand import Hand
from rules.rule import Rule
from rules.same_value_rule import SameValueRule
from rules.straight import Straight


class Aces(SameValueRule):
    def __init__(self):
        super().__init__(1, "Aces")


class Twos(SameValueRule):

    def __init__(self):
        super().__init__(2, "Twos")


class Threes(SameValueRule):

    def __init__(self):
        super().__init__(3, "Threes")


class Fours(SameValueRule):

    def __init__(self):
        super().__init__(4, "Fours")


class Fives(SameValueRule):

    def __init__(self):
        super().__init__(5, "Fives")


class Sixes(SameValueRule):

    def __init__(self):
        super().__init__(6, "Sixes")


class ThreeOfAKind(Rule):

    def name(self):
        return "Three of a kind"

    def points(self, hand: Hand):
        for i in range(6):
            if hand.count(i + 1) >= 3:
                return hand.sum()
        return 0


class FourOfAKind(Rule):

    def name(self):
        return "Four of a kind"

    def points(self, hand: Hand):
        for i in range(6):
            if hand.count(i + 1) >= 4:
                return hand.sum()
        return 0


class FullHouse(Rule):

    def name(self):
        return "Full house"

    def points(self, hand: Hand):
        counts = [hand.count(i + 1) for i in range(6)]
        if 2 in counts and 3 in counts:
            return 25
        else:
            return 0


class SmallStraight(Straight):

    def name(self):
        return "Small straight"

    def points(self, hand: Hand):
        list_of_hand = sorted(hand.get_hand())
        if len(list_of_hand) == 4 and self.is_straight(list_of_hand):
            return 30
        elif len(list_of_hand) == 5 and (self.is_straight(list_of_hand[1:]) or self.is_straight(list_of_hand[:-1])):
            return 30
        else:
            return 0


class LargeStraight(Straight):

    def name(self):
        return "Large straight"

    def points(self, hand: Hand):
        if self.is_straight(hand.get_hand()):
            return 40
        else:
            return 0


class Yahtzee(Rule):

    def name(self):
        return "Yahtzee"

    def points(self, hand: Hand):
        if len(set(hand.get_hand())) == 1:
            return 50
        else:
            return 0


class FibonYahtzee(Rule):

    def name(self):
        return "FibonYahtzee"

    def points(self, hand: Hand):
        if sorted(hand.get_hand()) == [1, 1, 2, 3, 5]:
            return 100
        else:
            return 0


class Chance(Rule):

    def name(self):
        return "Chance"

    def points(self, hand: Hand):
        return hand.sum()
