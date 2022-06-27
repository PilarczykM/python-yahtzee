from hand import Hand
from rules.rule import Rule


class SameValueRule(Rule):
    def __init__(self, value: int, name: str):
        self.__value = value
        self.__name = name

    def name(self):
        return self.__name

    def points(self, hand: Hand):
        return hand.count(self.__value) * self.__value
