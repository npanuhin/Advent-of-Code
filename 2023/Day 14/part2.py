def step(platform):
    for _ in range(4):
        for x in range(len(platform[0])):
            for y in range(len(platform)):
                if platform[y][x] == 'O':
                    while y > 0 and platform[y - 1][x] == '.':
                        platform[y][x] = '.'
                        y -= 1
                    platform[y][x] = 'O'

        # Rotate array:
        platform = [
            [platform[y][x] for y in range(len(platform) - 1, -1, -1)]
            for x in range(len(platform[0]))
        ]
    return platform


with open('input.txt') as file:
    platform = [list(line) for line in filter(None, map(str.strip, file))]

mem = {}

for cycle in range(100):
    platform = step(platform)

    platform_tuple = tuple(tuple(row) for row in platform)

    if platform_tuple in mem:
        for _ in range((1_000_000_000 - mem[platform_tuple]) % (cycle - mem[platform_tuple]) - 1):
            platform = step(platform)
        break

    mem[platform_tuple] = cycle

print(sum(
    len(platform) - y
    for y, row in enumerate(platform)
    for item in row
    if item == 'O'
))
