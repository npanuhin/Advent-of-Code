with open('input.txt') as file:
    platform = [list(line) for line in filter(None, map(str.strip, file))]

width, height = len(platform[0]), len(platform)

load = 0
for x in range(width):
    for y in range(height):
        if platform[y][x] == 'O':
            while y > 0 and platform[y - 1][x] == '.':
                platform[y][x] = '.'
                y -= 1
            platform[y][x] = 'O'

            load += height - y

print(load)
