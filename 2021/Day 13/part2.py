from re import fullmatch


max_x = max_y = 0
dots = []

with open("input.txt", 'r') as file:
    for line in file:
        if not line.strip():
            break
        x, y = map(int, line.split(','))
        max_x = max(max_x, x + 1)
        max_y = max(max_y, y + 1)
        dots.append((x, y))

    grid = [[False] * max_x for _ in range(max_y)]
    for x, y in dots:
        grid[y][x] = True

    for instruction in filter(lambda line: line, map(str.strip, file)):
        direction, target = fullmatch(r"fold along (x|y)=(\d+)", instruction).groups()
        target = int(target)

        if direction == 'y':
            for i in range(1, min(target + 1, max_y - target)):
                for j in range(max_x):
                    if grid[target + i][j]:
                        grid[target - i][j] = True
            max_y = target

        else:
            for i in range(max_y):
                for j in range(1, min(target + 1, max_x - target)):
                    if grid[i][target + j]:
                        grid[i][target - j] = True
            max_x = target

for i in range(max_y):
    print("".join('#' if grid[i][j] else ' ' for j in range(max_x)))
