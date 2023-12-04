from collections import defaultdict


def check_cell(y, x, condition):
    if 0 <= y < HEIGHT and 0 <= x < WIDTH and condition(engine[y][x]):
        return y, x


def get_adjacent(y, x_start, x_end):
    for test_x in range(x_start - 1, x_end + 1):
        yield (y - 1, test_x)
        yield (y + 1, test_x)

    yield (y, x_start - 1)
    yield (y, x_end)


def find_numbers(engine):
    for y in range(HEIGHT):
        x = 0
        while x < WIDTH:
            if engine[y][x].isdigit():
                x_start = x
                while x < WIDTH and engine[y][x].isdigit():
                    x += 1
                yield (y, x_start, x)
            x += 1


def part1(engine):
    part_num_sum = 0

    for y, x_start, x_end in find_numbers(engine):
        if any(
            check_cell(*coords, lambda cell: not cell.isdigit() and cell != '.')
            for coords in get_adjacent(y, x_start, x_end)
        ):
            part_num_sum += int(engine[y][x_start:x_end])

    return part_num_sum


def part2(engine):
    adjacent_numbers = defaultdict(list)

    for y, x_start, x_end in find_numbers(engine):
        for star in filter(None, (
            check_cell(*coords, lambda cell: cell == '*')
            for coords in get_adjacent(y, x_start, x_end))
        ):
            adjacent_numbers[star].append(int(engine[y][x_start:x_end]))

    return sum(
        numbers[0] * numbers[1]
        for numbers in adjacent_numbers.values()
        if len(numbers) == 2
    )


with open('input.txt') as file:
    engine = list(filter(None, map(str.strip, file)))

WIDTH, HEIGHT = len(engine[0]), len(engine)

print(part1(engine))
print(part2(engine))
