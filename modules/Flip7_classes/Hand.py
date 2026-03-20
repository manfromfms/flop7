from typing import List


cards_type_conversion_str_to_int = {
    '0':   0b0000000000000000000001,
    '1':   0b0000000000000000000010,
    '2':   0b0000000000000000000100,
    '3':   0b0000000000000000001000,
    '4':   0b0000000000000000010000,
    '5':   0b0000000000000000100000,
    '6':   0b0000000000000001000000,
    '7':   0b0000000000000010000000,
    '8':   0b0000000000000100000000,
    '9':   0b0000000000001000000000,
    '10':  0b0000000000010000000000,
    '11':  0b0000000000100000000000,
    '12':  0b0000000001000000000000,
    '+2':  0b0000000010000000000000,
    '+4':  0b0000000100000000000000,
    '+6':  0b0000001000000000000000,
    '+8':  0b0000010000000000000000,
    '+10': 0b0000100000000000000000,
    'x2':  0b0001000000000000000000,
    'sc':  0b0010000000000000000000,
    'f3':  0b0100000000000000000000,
    'fr':  0b1000000000000000000000,
}


class Hand:
    def __init__(self, cards_bitmap):
        """

        :param cards_bitmap: - Bitmap of cards, present at the hand.
        """
        self.cards_bitmap = cards_bitmap


    def __len__(self):
        length = 0

        for i in range(0, 12):
            if (self.cards_bitmap >> i) & 0b1:
                length += 1

        return length


    def __contains__(self, card):
        return bool(self.cards_bitmap & cards_type_conversion_str_to_int[card])


    def push(self, card):
        self.cards_bitmap |= cards_type_conversion_str_to_int[card]


    def pop(self, card):
        self.cards_bitmap &= ~cards_type_conversion_str_to_int[card]


    def count_score(self):
        score = 0
        x2 = bool((self.cards_bitmap >> 18) & 0b1)

        for i in range(0, 12):
            if (self.cards_bitmap >> i) & 0b1:
                score += i

        for p in [(13, 2), (14, 4), (15, 6), (16, 8), (17, 10)]:
            if (self.cards_bitmap >> p[0]) & 0b1:
                score += p[1]

        return score if not x2 else score * 2


    @staticmethod
    def fromList(cards: List[str]):
        cards_bitmap = 0

        for card in cards:
            if cards_bitmap & cards_type_conversion_str_to_int[card]:
                pass
                #TODO: Throw and error of invalid hand

            cards_bitmap |= cards_type_conversion_str_to_int[card]

        return Hand(
            cards_bitmap=cards_bitmap,
        )