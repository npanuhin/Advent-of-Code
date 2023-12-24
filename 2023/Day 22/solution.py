from collections import defaultdict


def calc(bricks):
    bricks = sorted(bricks, key=lambda brick: min(brick[0][2], brick[1][2]))

    max_x = max_y = max_z = 0
    for brick in bricks:
        for x, y, z in brick:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            max_z = max(max_z, z)

    space = [[[None] * (max_x + 1) for _ in range(max_y + 1)] for _ in range(max_z + 1)]

    bricks_hold = defaultdict(set)
    bricks_held_by = defaultdict(set)

    for i, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
        new_lowest_z = lowest_z = min(z1, z2)

        while new_lowest_z > 1 and all(
            space[new_lowest_z - 1][y][x] is None
            for x in range(x1, x2 + 1)
            for y in range(y1, y2 + 1)
        ):
            new_lowest_z -= 1

        z1 -= lowest_z - new_lowest_z
        z2 -= lowest_z - new_lowest_z

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                below = space[new_lowest_z - 1][y][x]
                if below is not None:
                    bricks_hold[below].add(i)
                    bricks_held_by[i].add(below)

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    space[z][y][x] = i

    return bricks_hold, bricks_held_by


def part1(bricks):
    bricks_hold, bricks_held_by = calc(bricks)

    return sum(
        all(
            len(bricks_held_by[j]) > 1
            for j in bricks_hold[i]
        )
        for i in range(len(bricks))
    )


def part2(bricks):
    bricks_hold, bricks_held_by = calc(bricks)

    answer = 0
    for i in range(len(bricks)):
        fallen_bricks = set([i])
        to_fall = [i]

        while to_fall:
            brick = to_fall.pop()

            if brick != i and any(
                held_by not in fallen_bricks
                for held_by in bricks_held_by[brick]
            ):
                continue

            fallen_bricks.add(brick)

            for brick_to_fall in bricks_hold[brick]:
                to_fall.append(brick_to_fall)

        answer += len(fallen_bricks) - 1

    return answer


with open('input.txt') as file:
    bricks = [
        [
            list(map(int, pos.split(',')))
            for pos in line.split('~')
        ]
        for line in filter(None, map(str.strip, file))
    ]

print(part1(bricks))
print(part2(bricks))
