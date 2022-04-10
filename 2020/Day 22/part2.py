from collections import deque
from itertools import islice


player1, player2 = deque(), deque()
input_player = 0

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in (line.strip() for line in file if line.strip()):
        if line.isnumeric():
            (player1 if input_player == 1 else player2).append(int(line))
        else:
            input_player += 1


def play_game(player1, player2):
    game_history = set()

    while player1 and player2:
        if (tuple(player1), tuple(player2)) in game_history:
            return 1

        game_history.add((tuple(player1), tuple(player2)))

        player1s_card = player1.popleft()
        player2s_card = player2.popleft()

        if len(player1) >= player1s_card and len(player2) >= player2s_card:

            if play_game(deque(islice(player1, 0, player1s_card)), deque(islice(player2, 0, player2s_card))) == 1:
                player1.extend((player1s_card, player2s_card))
            else:
                player2.extend((player2s_card, player1s_card))

        elif player1s_card > player2s_card:
            player1.extend((player1s_card, player2s_card))
        else:
            player2.extend((player2s_card, player1s_card))

    return 1 if player1 else 2


winner = player1 if play_game(player1, player2) == 1 else player2

print(sum(
    card * (len(winner) - i)
    for i, card in enumerate(winner)
))
