DIRECTIONS = {
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
    'U': (-1, 0)
}
DIRECTIONS_LIST = list(DIRECTIONS.keys())


def calc(plan):
    signed_area = perimeter = 0

    y = x = 0
    for direction, length in plan:
        perimeter += length

        dy, dx = DIRECTIONS[direction]
        new_y = y + dy * length
        new_x = x + dx * length

        signed_area += (y + new_y) * (x - new_x)

        y, x = new_y, new_x

    # A total of 4 corders are not canceled out and look outwards 4 * 0.5 * 0.5
    return signed_area // 2 + perimeter // 2 + 1


def part1(plan):
    return calc([
        [direction, int(length)]
        for direction, length, _ in plan
    ])


def part2(plan):
    return calc([
        [
            DIRECTIONS_LIST[int(color[-2])],
            int(color[2:-2], 16)
        ]
        for _, _, color in plan
    ])


with open('input.txt') as file:
    plan = list(map(str.split, filter(None, map(str.strip, file))))


print(part1(plan))
print(part2(plan))
