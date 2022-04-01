with open("input.txt", 'r') as file:
    lines = [
        sum(map(lambda x: tuple(map(int, x.split(','))), line.split("->")), start=())
        for line in file
    ]

max_x = max(max(x1, x2) for x1, y1, x2, y2 in lines)
max_y = max(max(y1, y2) for x1, y1, x2, y2 in lines)

field = [[0] * (max_x + 1) for _ in range(max_y + 1)]

for x1, y1, x2, y2 in lines:
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    if x1 == x2:
        for y in range(y1, y2 + 1):
            field[y][x1] += 1
    elif y1 == y2:
        for x in range(x1, x2 + 1):
            field[y1][x] += 1

print(sum(sum(1 for item in line if item >= 2) for line in field))
