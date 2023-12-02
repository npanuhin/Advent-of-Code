def rotate(i, j, n):
    for step in range(n % 4):
        i, j = -j, i
    return i, j


actions = {
    'N': lambda x, y, i, j, n: (x, y, i + n, j),
    'S': lambda x, y, i, j, n: (x, y, i - n, j),
    'E': lambda x, y, i, j, n: (x, y, i, j + n),
    'W': lambda x, y, i, j, n: (x, y, i, j - n),
    'F': lambda x, y, i, j, n: (x + i * n, y + j * n, i, j),
    'L': lambda x, y, i, j, n: (x, y, *rotate(i, j, -n // 90)),
    'R': lambda x, y, i, j, n: (x, y, *rotate(i, j, n // 90))
}

y, x = 0, 0   # Ship
i, j = 1, 10  # Waypoint

with open("input.txt") as file:
    for line in file:
        action, n = line[0], int(line[1:])
        x, y, i, j = actions[action](x, y, i, j, n)

print(abs(x) + abs(y))
