from collections import Counter


CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def get_type(cards: str) -> int:
    cards = Counter(cards)
    jokers = 0 if 'J' in CARDS else cards['J']

    # Five of a kind
    for card in CARDS:
        if cards[card] <= 5 <= cards[card] + jokers:
            return 6

    # Four of a kind
    for card in CARDS:
        if cards[card] <= 4 <= cards[card] + jokers:
            return 5

    # Full house
    for card1 in CARDS:
        if cards[card1] <= 3 <= cards[card1] + jokers:
            jokers_used = 3 - cards[card1]
            for card2 in CARDS:
                if card1 != card2 and cards[card2] <= 2 <= cards[card2] + max(0, jokers - jokers_used):
                    return 4

    # Three of a kind
    for card in CARDS:
        if cards[card] <= 3 <= cards[card] + jokers:
            return 3

    # Two pairs
    pairs = 0
    jokers_used = 0
    for card in CARDS:
        if cards[card] <= 2 <= cards[card] + max(0, jokers - jokers_used):
            pairs += 1
            jokers_used += 2 - cards[card]
    if pairs == 2:
        return 2

    # One pair
    if pairs == 1:
        return 1

    # High card
    return 0


def hand_value(hand: str) -> tuple[int]:
    return tuple(CARDS.index(card) if card in CARDS else len(CARDS) for card in hand[0])


def calc(hands):
    hands_by_type = [[] for _ in range(7)]
    for cards, bid in hands:
        hands_by_type[get_type(cards)].append((cards, bid))

    answer = 0
    rank = 1
    for cur_hands in hands_by_type:
        for cards, bid in sorted(cur_hands, key=hand_value, reverse=True):
            answer += bid * rank
            rank += 1

    return answer


def part1(hands):
    return calc(hands)


def part2(hands):
    CARDS.remove('J')
    return calc(hands)


with open('input.txt') as file:
    hands = [
        [cards, int(bid)]
        for cards, bid in map(str.split, filter(None, map(str.strip, file)))
    ]

print(part1(hands))
print(part2(hands))
