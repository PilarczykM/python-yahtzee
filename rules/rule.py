from abc import ABC, abstractmethod

from hand import Hand


class Rule(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def points(self, hand: Hand):
        pass
