def aces(hand):
    result = 0
    for face in (x for x in hand.get_hand() if x == 1):
        result += face
    return result


def twos(hand):
    result = 0
    for face in (x for x in hand.get_hand() if x == 2):
        result += face
    return result


def threes(hand):
    result = 0
    for face in (x for x in hand.get_hand() if x == 3):
        result += face
    return result


def fours(hand):
    result = 0
    for face in (x for x in hand.get_hand() if x == 4):
        result += face
    return result


def fives(hand):
    result = 0
    for face in (x for x in hand.get_hand() if x == 5):
        result += face
    return result


def sixes(hand):
    result = 0
    for face in (x for x in hand.get_hand() if x == 6):
        result += face
    return result


def three_of_a_kind(hand):
    for i in hand.get_hand():
        if hand.get_hand().count(i) >= 3:
            return sum(hand.get_hand())
    return 0


def four_of_a_kind(hand):
    for i in hand.get_hand():
        if hand.get_hand().count(i) >= 4:
            return sum(hand.get_hand())
    return 0


def full_house(hand):
    for i in hand.get_hand():
        x = hand.get_hand().count(i)
        if x == 3:
            for j in hand.get_hand():
                y = hand.get_hand().count(j)
                if y == 2 and x != y:
                    return 25
    return 0


def small_straight(hand):
    hand = list(set(sorted(hand.get_hand())))
    try:
        if len(hand) >= 4:
            for idx, val in enumerate(hand):
                if hand[idx + 1] == val + 1 and \
                        hand[idx + 2] == val + 2 and \
                        hand[idx + 3] == val + 3:
                    return 30
    except IndexError:
        pass
    return 0


def large_straight(hand):
    hand = list(set(sorted(hand.get_hand())))
    try:
        if len(hand) >= 5:
            for idx, val in enumerate(hand):
                if hand[idx + 1] == val + 1 and \
                        hand[idx + 2] == val + 2 and \
                        hand[idx + 3] == val + 3 and \
                        hand[idx + 4] == val + 4:
                    return 40
    except IndexError:
        pass
    return 0


def yahtzee(hand):
    if len(set(hand.get_hand())) == 1:
        return 50
    return 0


def chance(hand):
    return sum(hand.get_hand())


RULES_MAP = {
    1: aces,
    2: twos,
    3: threes,
    4: fours,
    5: fives,
    6: sixes,
    7: three_of_a_kind,
    8: four_of_a_kind,
    9: full_house,
    10: small_straight,
    11: large_straight,
    12: yahtzee,
    13: chance,
}
