from copy import deepcopy
from collections import deque

MOVES = {
    "nw": (1, -1),
    "sw": (1, 1),
    "se": (-1, 1),
    "ne": (-1, -1),
    "w": (2, 0),
    "e": (-2, 0)
}
ONLY_MOVES = tuple(MOVES.values())

black = set()

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        line_pos = 0
        coords = [0, 0]

        while line_pos < len(line.strip()):

            for move in MOVES:
                if line.startswith(move, line_pos):
                    coords[0] += MOVES[move][0]
                    coords[1] += MOVES[move][1]
                    line_pos += len(move)

        coords = tuple(coords)
        if coords in black:
            black.remove(coords)
        else:
            black.add(coords)


left, right = min(y for y, x in black), max(y for y, x in black)
bottom, top = min(x for y, x in black), max(x for y, x in black)

first_grid = deque(deque(False for _ in range(right - left + 7)) for _ in range(top - bottom + 5))
second_grid = deepcopy(first_grid)

for x, y in black:
    first_grid[y - bottom + 2][x - left + 3] = True

for day in range(100):
    enlarge_left, enlarge_right, enlarge_top, enlarge_bottom = False, False, False, False

    for y in range(1, len(first_grid) - 1):
        for x in range(2, len(first_grid[0]) - 2):

            if first_grid[y][x]:
                black_ajacent = sum(first_grid[y + dy][x + dx] for dx, dy in ONLY_MOVES)
                second_grid[y][x] = not (black_ajacent == 0 or black_ajacent > 2)
            else:
                black_ajacent = sum(first_grid[y + dy][x + dx] for dx, dy in ONLY_MOVES)
                second_grid[y][x] = (black_ajacent == 2)

            if second_grid[y][x]:
                enlarge_top |= (y == 2)
                enlarge_bottom |= (y == len(first_grid) - 3)
                enlarge_left |= (x == 2)
                enlarge_right |= (x == len(first_grid[0]) - 3)

    if enlarge_left:
        for i in range(len(first_grid)):
            first_grid[i].appendleft(False)
            first_grid[i].appendleft(False)
            second_grid[i].appendleft(False)
            second_grid[i].appendleft(False)

    if enlarge_right:
        for i in range(len(first_grid)):
            first_grid[i].append(False)
            first_grid[i].append(False)
            second_grid[i].append(False)
            second_grid[i].append(False)

    if enlarge_top:
        first_grid.appendleft(deque(False for _ in range(len(first_grid[0]))))
        second_grid.appendleft(deque(False for _ in range(len(first_grid[0]))))

    if enlarge_bottom:
        first_grid.append(deque(False for _ in range(len(first_grid[0]))))
        second_grid.append(deque(False for _ in range(len(first_grid[0]))))

    first_grid, second_grid = second_grid, first_grid

print(sum(sum(line) for line in first_grid))
