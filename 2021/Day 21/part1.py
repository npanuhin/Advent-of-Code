with open("input.txt") as file:
    players = [int(file.readline().split()[-1]) - 1 for _ in range(2)]

dice = -1
turn = 0
score = [0] * 2

while max(score) < 1000:
    move = sum((dice := dice + 1) % 100 + 1 for _ in range(3))
    players[turn] += move
    players[turn] %= 10
    score[turn] += players[turn] + 1

    turn = not turn

print(min(score) * (dice + 1))
