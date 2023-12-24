DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
STEPS = 64


with open('input.txt') as file:
    garden = list(filter(None, map(str.strip, file)))

width, height = len(garden[0]), len(garden)

plots = set([next(
    (y, x)
    for y, row in enumerate(garden)
    for x, plot in enumerate(row)
    if plot == 'S'
)])

ans = [[False] * width for _ in range(height)]

for step in range(STEPS - 1, -1, -1):
    new_plots = set()

    for y, x in plots:
        for dy, dx in DIRECTIONS:
            new_y = y + dy
            new_x = x + dx
            if 0 <= new_y < height and 0 <= new_x < width and garden[new_y][new_x] != '#' and not ans[new_y][new_x]:
                new_plots.add((new_y, new_x))

    if step % 2 == 0:
        for y, x in new_plots:
            ans[y][x] = True

    plots = new_plots

print(sum(sum(row) for row in ans))
