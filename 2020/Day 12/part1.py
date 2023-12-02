DIRECTIONS = ((0, 1), (-1, 0), (0, -1), (1, 0))
dr = 0

actions = {
    'N': lambda x, y, dr, n: (x, y + n, dr),
    'S': lambda x, y, dr, n: (x, y - n, dr),
    'E': lambda x, y, dr, n: (x + n, y, dr),
    'W': lambda x, y, dr, n: (x - n, y, dr),
    'F': lambda x, y, dr, n: (x + DIRECTIONS[dr][1] * n, y + DIRECTIONS[dr][0] * n, dr),
    'L': lambda x, y, dr, n: (x, y, (dr - n // 90) % 4),
    'R': lambda x, y, dr, n: (x, y, (dr + n // 90) % 4)
}

y, x = 0, 0

with open("input.txt") as file:
    for line in file:
        action, n = line[0], int(line[1:])
        x, y, dr = actions[action](x, y, dr, n)

print(abs(x) + abs(y))
