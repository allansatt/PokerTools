from random import random

values = list(range(1, 11)) + ["J", "Q", "K", "A"]
suits = {"s", "h", "d", "c"}


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __str__(self):
        return str(self.value) + self.suit

    def __eq__(self, other):
        return isinstance(other,Card) and self.value == other.value and self.suit == other.suit


class Hand:
    def __init__(self, card1, card2):
        if values.index(card1.value) > values.index(card2.value):
            self.over = card1
            self.under = card2
        else:
            self.over = card1
            self.under = card2
        if card1.value == card2.value:
            self.logical_value = str(self.over.value) + str(self.under.value)
        elif card1.suit == card2.suit:
            self.logical_value = str(self.over.value) + str(self.under.value) + "s"
        else:
            self.logical_value = str(self.over.value) + str(self.under.value) + "o"

    def __str__(self):
        return str(self.over) + str(self.under)

    def __eq__(self,other):
        return isinstance(other,Hand) and self.over == other.over and self.under == other.under


class Deck(set):
    def __init__(self):
        super().__init__()
        for suit in suits:
            for value in values:
                self.add(Card(value, suit))

    def flop(self):
        return [self.draw(), self.draw(), self.draw()]

    def draw(self):
        result = random.choice(tuple(self))
        self.remove(result)
        return result

    def deal(self):
        return Hand(self.draw(),self.draw())


def pairs_in_range(top="A", bottom=2):
    hands = []
    for card_value in values[values.index(bottom):values.index(top) + 1]:
        remaining_suits = set(suits)
        for first_suit in suits:
            remaining_suits.remove(first_suit)
            for second_suit in remaining_suits:
                hands.append(Hand(Card(card_value, first_suit), Card(card_value, second_suit)))
    return hands


def offsuit_range(top, bottom=2):
    hands = []
    for under_card in values[values.index(bottom):values.index(top)]:
        hands += offsuit_cards(top, under_card)
    return hands


def suited_range(top, bottom=2):
    hands = []
    for under_card in values[values.index(bottom):values.index(top)]:
        hands += suited_cards(top, under_card)
    return hands


def suited_cards(top, bottom):
    hands = []
    for suit in suits:
        hands.append(Hand(Card(top, suit), Card(bottom, suit)))
    return hands


def offsuit_cards(top, bottom):
    hands = []
    for suit in suits:
        offsuits = set(suits)
        offsuits.remove(suit)
        for offsuit in offsuits:
            hands.append(Hand(Card(top, suit), Card(bottom, offsuit)))
    return hands


def suited_broadway_range(top, bottom, depth):
    hands = []
    for top_value in values[values.index(bottom):values.index(top) + 1]:
        hands += suited_range(top_value, values[values.index(top_value) - depth])
    return hands


def offsuit_broadway_range(top, bottom, depth):
    hands = []
    for top_value in values[values.index(bottom):values.index(top) + 1]:
        hands += offsuit_range(top_value, values[values.index(top_value) - depth])
    return hands


def all_hands():
    hands = []
    for top_value in values:
        hands += suited_range(top_value)
        hands += offsuit_range(top_value)
    return hands + pairs_in_range()
