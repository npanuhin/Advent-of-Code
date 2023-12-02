def simulate(sea):
    new_sea = [['.'] * WIDTH for _ in range(HIEGHT)]

    for y in range(HIEGHT):
        for x in range(WIDTH):
            if sea[y][x] == '>':
                next_x = (x + 1) % WIDTH
                if sea[y][next_x] == '.':
                    new_sea[y][next_x] = '>'
                else:
                    new_sea[y][x] = '>'

    for y in range(HIEGHT):
        for x in range(WIDTH):
            if sea[y][x] == 'v':
                next_y = (y + 1) % HIEGHT
                if sea[next_y][x] != 'v' and new_sea[next_y][x] == '.':
                    new_sea[next_y][x] = 'v'
                else:
                    new_sea[y][x] = 'v'

    return new_sea


with open('input.txt') as file:
    sea = [list(line) for line in filter(None, map(str.strip, file))]

WIDTH, HIEGHT = len(sea[0]), len(sea)

steps = 0
while True:
    steps += 1
    new_sea = simulate(sea)
    if new_sea == sea:
        break
    sea = new_sea

print(steps)
