from collections import deque


with open("input.txt", 'r', encoding="utf-8") as file:
    player1, player2 = (
        deque(map(int, player.splitlines()[1:]))
        for player in file.read().split("\n\n")
    )

while player1 and player2:
    if player1[0] > player2[0]:
        player1.extend((player1.popleft(), player2.popleft()))
    else:
        player2.extend((player2.popleft(), player1.popleft()))

print(sum(i * card for i, card in enumerate(reversed(player1 + player2), 1)))
