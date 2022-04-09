from collections import Counter
from itertools import product


ADJACENT_DIRECTIONS = (-1, 0, 1)

with open("input.txt", 'r', encoding="utf-8") as file:
    cur_active = set(
        (x, y, 0, 0)
        for y, line in enumerate(file)
        for x, box in enumerate(line)
        if box == '#'
    )

for cycle in range(6):
    next_active = set()
    adjacent_points = []

    for point in cur_active:
        adjacent = set(product(*(
            tuple(dimension + delta for delta in ADJACENT_DIRECTIONS) for dimension in point
        )))
        adjacent.remove(point)

        adjacent_points += adjacent

        if 2 <= len(adjacent.intersection(cur_active)) <= 3:
            next_active.add(point)

    next_active.update(
        point
        for point, count in Counter(adjacent_points).items()
        if count == 3 and point not in cur_active
    )

    cur_active = next_active

print(len(cur_active))
