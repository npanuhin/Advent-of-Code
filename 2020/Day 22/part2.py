from collections import deque
from itertools import islice


def play(player1, player2):
    game_history = set()

    while player1 and player2:
        if (state := (tuple(player1), tuple(player2))) in game_history:
            return True, player1
        game_history.add(state)

        card1 = player1.popleft()
        card2 = player2.popleft()

        if len(player1) >= card1 and len(player2) >= card2:
            cards1, cards2 = deque(islice(player1, 0, card1)), deque(islice(player2, 0, card2))
            player1_wins = (
                (cards1_max := max(cards1)) > max(cards2) and cards1_max > card1 + card2 - 2
            ) or play(cards1, cards2)
        else:
            player1_wins = card1 > card2

        if player1_wins:
            player1.extend((card1, card2))
        else:
            player2.extend((card2, card1))

    return player1


with open("input.txt") as file:
    players = [
        deque(map(int, player.splitlines()[1:]))
        for player in file.read().split("\n\n")
    ]

print(sum(i * card for i, card in enumerate(reversed(players[not play(*players)]), 1)))
