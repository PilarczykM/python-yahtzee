from rules.rule import *


def test_aces():
    hand = Hand()
    for i in hand.hand:
        i._Die__face = 1
    assert aces(hand) == 5


def test_three_of_a_kind():
    hand = Hand()
    for i in range(3):
        hand.hand[i]._Die__face = 1
    for i in range(3, 5):
        hand.hand[i]._Die__face = 2
    assert three_of_a_kind(hand) == 7


def test_four_of_a_kind():
    hand = Hand()
    for i in range(4):
        hand.hand[i]._Die__face = 1
    for i in range(4, 5):
        hand.hand[i]._Die__face = 2
    assert four_of_a_kind(hand) == 6


def test_full_house():
    hand = Hand()
    for i in range(1):
        hand.hand[i]._Die__face = 2
    for i in range(1, 3):
        hand.hand[i]._Die__face = 2
    for i in range(3, 5):
        hand.hand[i]._Die__face = 3
    assert full_house(hand) == 25


def test_small_straight():
    hand = Hand()
    hand.hand[0]._Die__face = 4
    hand.hand[1]._Die__face = 3
    hand.hand[2]._Die__face = 5
    hand.hand[3]._Die__face = 2
    hand.hand[4]._Die__face = 5
    assert small_straight(hand) == 30


def test_large_straight():
    hand = Hand()
    hand.hand[0]._Die__face = 4
    hand.hand[1]._Die__face = 3
    hand.hand[2]._Die__face = 5
    hand.hand[3]._Die__face = 2
    hand.hand[4]._Die__face = 1
    assert large_straight(hand) == 40


def test_yahtzee():
    hand = Hand()
    for i in hand.hand:
        i._Die__face = 3
    assert yahtzee(hand) == 50


def test_chance():
    hand = Hand()
    for i in range(5):
        hand.hand[i]._Die__face = i + 1
    assert chance(hand) == 15
