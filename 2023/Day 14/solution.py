def single_step(platform):
    for x in range(len(platform[0])):
        for y in range(len(platform)):
            if platform[y][x] == 'O':
                while y > 0 and platform[y - 1][x] == '.':
                    platform[y][x] = '.'
                    y -= 1
                platform[y][x] = 'O'

    return platform


def rotation_step(platform):
    for _ in range(4):
        platform = single_step(platform)

        # Rotate array:
        platform = [
            [platform[y][x] for y in range(len(platform) - 1, -1, -1)]
            for x in range(len(platform[0]))
        ]
    return platform


def calc(platform):
    return sum(
        len(platform) - y
        for y, row in enumerate(platform)
        for item in row
        if item == 'O'
    )


def part1(platform):
    return calc(single_step(platform))


def part2(platform):
    mem = {}

    for cycle in range(1_000_000_000):
        platform = rotation_step(platform)

        platform_tuple = tuple(tuple(row) for row in platform)
        if platform_tuple in mem:
            for _ in range((1_000_000_000 - mem[platform_tuple]) % (cycle - mem[platform_tuple]) - 1):
                platform = rotation_step(platform)
            break

        mem[platform_tuple] = cycle

    return calc(platform)


with open('input.txt') as file:
    platform = [list(line) for line in filter(None, map(str.strip, file))]

print(part1(platform))
print(part2(platform))
