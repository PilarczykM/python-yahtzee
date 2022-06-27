from hand import Hand


def test_hand_number_of_dice():
    hand = Hand(15, 6)
    assert len(hand.hand) == 15


def test_hand_sides_per_die():
    hand = Hand(5, 18)
    for die in hand.hand:
        assert die.sides == 18
