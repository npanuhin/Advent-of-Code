from collections import Counter


CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def get_type(cards: str) -> int:
    cards = Counter(cards)

    # Five of a kind
    for card in CARDS:
        if cards[card] == 5:
            return 6

    # Four of a kind
    for card in CARDS:
        if cards[card] == 4:
            return 5

    # Full house
    for card1 in CARDS:
        if cards[card1] == 3:
            for card2 in CARDS:
                if card1 != card2 and cards[card2] == 2:
                    return 4

    # Three of a kind
    for card in CARDS:
        if cards[card] == 3:
            return 3

    # Two pairs
    pairs = 0
    for card in CARDS:
        if cards[card] == 2:
            pairs += 1
    if pairs == 2:
        return 2

    # One pair
    if pairs == 1:
        return 1

    # High card
    return 0


def hand_value(hand: str) -> tuple[int]:
    return tuple(CARDS.index(card) for card in hand[0])


with open('input.txt') as file:
    hands = [
        [cards, int(bid)]
        for cards, bid in map(str.split, filter(None, map(str.strip, file)))
    ]

hands_by_type = [[] for _ in range(7)]
for cards, bid in hands:
    hands_by_type[get_type(cards)].append((cards, bid))

answer = 0
rank = 1
for cur_hands in hands_by_type:
    for cards, bid in sorted(cur_hands, key=hand_value, reverse=True):
        answer += bid * rank
        rank += 1

print(answer)
