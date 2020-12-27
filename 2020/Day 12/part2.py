def rotate(i, j, n):
    if abs(n) % 4 == 0:
        return i, j

    if abs(n) % 4 == 1:
        return (-j, i) if n > 0 else (j, -i)

    if abs(n) % 4 == 2:
        return -i, -j

    if abs(n) % 4 == 3:
        return (j, -i) if n > 0 else (-j, i)


actions = {
    'N': lambda x, y, i, j, n: (x, y, i + n, j),
    'S': lambda x, y, i, j, n: (x, y, i - n, j),
    'E': lambda x, y, i, j, n: (x, y, i, j + n),
    'W': lambda x, y, i, j, n: (x, y, i, j - n),
    'F': lambda x, y, i, j, n: (x + i * n, y + j * n, i, j),
    'L': lambda x, y, i, j, n: (x, y, *rotate(i, j, -n // 90)),
    'R': lambda x, y, i, j, n: (x, y, *rotate(i, j, n // 90))
}

y, x = 0, 0
i, j = 1, 10

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        action, n = line[0], int(line[1:])
        x, y, i, j = actions[action](x, y, i, j, n)

print(abs(x) + abs(y))
