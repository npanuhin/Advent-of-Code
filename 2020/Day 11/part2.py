from copy import deepcopy


DIRECTIONS = [(dy, dx) for dx in range(-1, 2) for dy in range(-1, 2) if dy != 0 or dx != 0]


def has_occupied(layout, sight, y, x, amount):
    result = 0

    for sight_y, sight_x in sight[y][x]:
        if sight_y is not None:
            result += layout[sight_y][sight_x] == '#'
            if result >= amount:
                return True

    return False


with open("input.txt", 'r', encoding="utf-8") as file:
    layout = [list(line.strip()) for line in file]

size_y, size_x = len(layout), len(layout[0])

layout1, layout2 = layout, deepcopy(layout)

sight = [[[] for x in range(size_x)] for y in range(size_y)]

for y in range(size_y):
    for x in range(size_x):
        for dy, dx in DIRECTIONS:

            cur_y, cur_x = y + dy, x + dx
            while 0 <= cur_y < size_y and 0 <= cur_x < size_x and layout1[cur_y][cur_x] == '.':
                cur_y += dy
                cur_x += dx

            sight[y][x].append((cur_y, cur_x) if 0 <= cur_y < size_y and 0 <= cur_x < size_x else (None, None))

while True:
    for y in range(size_y):
        for x in range(size_x):
            if layout1[y][x] == 'L' and not has_occupied(layout1, sight, y, x, 1):
                layout2[y][x] = '#'

            elif layout1[y][x] == '#' and has_occupied(layout1, sight, y, x, 5):
                layout2[y][x] = 'L'

            else:
                layout2[y][x] = layout1[y][x]

    if layout1 == layout2:
        break

    layout1, layout2 = layout2, layout1

occupied_seats = sum(layout1[y][x] == '#' for x in range(size_x) for y in range(size_y))
print(occupied_seats)
