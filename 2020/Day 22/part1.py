from collections import deque

player1, player2 = deque(), deque()
input_player = 0

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in (line.strip() for line in file if line.strip()):

        if line.isnumeric():
            (player1 if input_player == 1 else player2).append(int(line))
        else:
            input_player += 1


while player1 and player2:
    if player1[0] > player2[0]:
        player1.extend((player1.popleft(), player2.popleft()))
    else:
        player2.extend((player2.popleft(), player1.popleft()))

winner = player1 + player2

print(sum(
    card * (len(winner) - i)
    for i, card in enumerate(winner)
))
