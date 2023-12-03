def check_cell(y: int, x: int) -> tuple[int, int]:
    if 0 <= y < HEIGHT and 0 <= x < WIDTH and not engine[y][x].isdigit() and engine[y][x] != '.':
        return y, x


def get_adjacent(y: int, x_start: int, x_end: int) -> tuple[int, int]:
    for test_x in range(x_start - 1, x_end + 1):
        yield (y - 1, test_x)
        yield (y + 1, test_x)

    yield (y, x_start - 1)
    yield (y, x_end)


with open('input.txt') as file:
    engine = list(filter(None, map(str.strip, file)))

WIDTH, HEIGHT = len(engine[0]), len(engine)

part_num_sum = 0

for y in range(HEIGHT):
    x = 0
    while x < WIDTH:
        if engine[y][x].isdigit():
            x_start = x
            while x < WIDTH and engine[y][x].isdigit():
                x += 1

            if any(check_cell(*coords) for coords in get_adjacent(y, x_start, x)):
                part_num_sum += int(engine[y][x_start:x])

        x += 1

print(part_num_sum)
