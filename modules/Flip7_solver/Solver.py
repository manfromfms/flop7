from typing import Dict

from ..Flip7_classes import Hand, Deck

def search_simple(
        hand: Hand,
        deck: Deck,
        discard: Deck,
        initial_score,
        hash_=None,
        root=False,
        subroot=False
):
    if hash_ is None:
        hash_ = {}

    expected_value = 0

    if len(hand) == 7:
        hash_[hand.cards_bitmap] = hand.count_score() + 15
        return hash_[hand.cards_bitmap]

    for card in deck.cards:
        if card not in deck:
            continue

        if card not in hand:
            hand.push(card)
            deck.pop(card)

            score = 0

            if hand.cards_bitmap in hash_:
                score = hash_[hand.cards_bitmap]
            else:
                score = search_simple(
                    hand=hand,
                    deck=deck,
                    discard=discard,
                    initial_score=hand.count_score(),
                    hash_=hash_,
                    subroot=root,
                )

            hand.pop(card)
            deck.push(card)

            expected_value += score * deck.cards[card] / deck.length

            if root:
                print(f'info card {card} prob {deck.cards[card] / deck.length} value {score} score {score * deck.cards[card] / deck.length}')

        else:
            if root:
                print(f'info card {card} prob {deck.cards[card] / deck.length} value 0.0 score 0.0')

    hash_[hand.cards_bitmap] = max(initial_score, expected_value)

    return max(initial_score, expected_value)


def solver_simple(hand: Hand, deck: Deck, discard: Deck):
    return search_simple(hand, deck, discard, hand.count_score(), root=True) - hand.count_score()