def sign(x):
    return 0 if x == 0 else 1 if x > 0 else -1


with open("input.txt", 'r') as file:
    lines = [
        sum(map(lambda x: tuple(map(int, x.split(','))), line.split("->")), start=())
        for line in file
    ]

max_x = max(max(x1, x2) for x1, y1, x2, y2 in lines)
max_y = max(max(y1, y2) for x1, y1, x2, y2 in lines)

field = [[0] * (max_x + 1) for _ in range(max_y + 1)]

for x1, y1, x2, y2 in lines:
    dx = sign(x2 - x1)
    dy = sign(y2 - y1)
    for i in range(max(abs(x2 - x1), abs(y2 - y1)) + 1):
        field[y1 + i * dy][x1 + i * dx] += 1


print(sum(sum(1 for item in line if item >= 2) for line in field))
