from copy import deepcopy


def count_neighbors(space, x, y, z):
    result = -space[z][y][x]
    for z1 in range(z - 1, z + 2):
        for y1 in range(y - 1, y + 2):
            for x1 in range(x - 1, x + 2):
                if space[z1][y1][x1]:
                    result += 1
    return result


CYCLES = 6

with open("input.txt", 'r', encoding="utf-8") as file:
    inp = [[box == '#' for box in line] for line in file.readlines()]

height, width, depth = len(inp) + (CYCLES + 1) * 2, len(inp[0]) + (CYCLES + 1) * 2, 1 + (CYCLES + 1) * 2

space = [
    [[[False for x in range(width)] for y in range(height)] for z in range(CYCLES + 1)] +
    [
        [[False for x in range(width)] for y in range(CYCLES + 1)] +

        [
            [False for x in range(CYCLES + 1)] +
            line +
            [False for x in range(CYCLES + 1)] for line in inp
        ] +

        [[False for x in range(width)] for y in range(CYCLES + 1)]
    ] +
    [[[False for x in range(width)] for y in range(height)] for z in range(CYCLES + 1)]
][0]

space1, space2 = space, deepcopy(space)

for cycle in range(CYCLES):
    for z in range(1, depth - 1):
        for y in range(1, height - 1):
            for x in range(1, width - 1):
                if space1[z][y][x] and not (2 <= count_neighbors(space1, x, y, z) <= 3):
                    space2[z][y][x] = False
                elif not space1[z][y][x] and count_neighbors(space1, x, y, z) == 3:
                    space2[z][y][x] = True
                else:
                    space2[z][y][x] = space1[z][y][x]
    space1, space2 = space2, space1

print(sum(
    space1[z][y][x]
    for x in range(width)
    for y in range(height)
    for z in range(depth)
))
