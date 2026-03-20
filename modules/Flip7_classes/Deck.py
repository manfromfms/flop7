from typing import Dict

class Deck:
    def __init__(self, cards: Dict[str, int]):
        self.cards = cards

        self.length = 0
        for card in self.cards:
            self.length += self.cards[card]

    def push(self, card):
        self.cards[card] += 1
        self.length += 1

    def pop(self, card):
        self.cards[card] -= 1
        self.length -= 1

    def __len__(self):
        return self.length

    def __contains__(self, card):
        return self.cards[card] > 0

    @staticmethod
    def StandardDeck():
        return Deck(
            cards={
                '0': 1,
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                '10': 10,
                '11': 11,
                '12': 12,
                '+2': 1,
                '+4': 1,
                '+6': 1,
                '+8': 1,
                '+10': 1,
                'x2': 1,
                'f3': 3,
                'sc': 3,
                'fr': 3,
            }
        )

    @staticmethod
    def SimpleDeck():
        return Deck(
            cards={
                '0': 1,
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                '10': 10,
                '11': 11,
                '12': 12,
                '+2': 1,
                '+4': 1,
                '+6': 1,
                '+8': 1,
                '+10': 1,
                'x2': 1,
            }
        )