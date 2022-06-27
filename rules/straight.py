from rules.rule import Rule


class Straight(Rule):

    @staticmethod
    def is_straight(list_of_hand) -> bool:
        # verify that the list has no duplicates
        if len(list(set(list_of_hand))) != len(list_of_hand):
            return False
        # sum of consecutive n numbers 1...n = n * (n+1) / 2
        consecutive_sum = (min(list_of_hand) + max(list_of_hand)) * (max(list_of_hand) - min(list_of_hand) + 1) / 2
        return sum(list_of_hand) == consecutive_sum
