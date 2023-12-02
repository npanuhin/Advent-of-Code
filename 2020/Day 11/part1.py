DIRECTIONS = [(dy, dx) for dx in range(-1, 2) for dy in range(-1, 2) if dy != 0 or dx != 0]


def has_occupied(layout, y, x, amount):
    result = 0

    for dy, dx in DIRECTIONS:
        result += layout[y + dy][x + dx] == '#'
        if result >= amount:
            return True

    return False


with open("input.txt") as file:
    layout = [list(line.strip()) for line in file]

size_y, size_x = len(layout) + 2, len(layout[0]) + 2

layout1 = [['.'] * size_x] + [['.'] + line + ['.'] for line in layout] + [['.'] * size_x]
layout2 = [['.'] * size_x] + [['.'] + line + ['.'] for line in layout] + [['.'] * size_x]

while True:
    for y in range(size_y):
        for x in range(size_x):
            if layout1[y][x] == 'L' and not has_occupied(layout1, y, x, 1):
                layout2[y][x] = '#'

            elif layout1[y][x] == '#' and has_occupied(layout1, y, x, 4):
                layout2[y][x] = 'L'

            else:
                layout2[y][x] = layout1[y][x]

    layout1, layout2 = layout2, layout1
    if layout1 == layout2:
        break

print(sum(
    layout1[y][x] == '#' for x in range(size_x) for y in range(size_y)
))
