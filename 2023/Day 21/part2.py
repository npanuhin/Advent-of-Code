DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
STEPS = 26501365


with open('input.txt') as file:
    garden = list(filter(None, map(str.strip, file)))

size = len(garden)
assert len(garden[0]) == size
assert STEPS % size == size // 2

start_y, start_x = next(
    (y, x)
    for y, row in enumerate(garden)
    for x, plot in enumerate(row)
    if plot == 'S'
)
assert start_y == start_x == size // 2


def fill(start_y: int, start_x: int, steps: int) -> int:
    plots = set([(start_y, start_x)])
    ans = [[False] * size for _ in range(size)]

    for step in range(steps - 1, -1, -1):
        new_plots = set()

        for y, x in plots:
            for dy, dx in DIRECTIONS:
                new_y = y + dy
                new_x = x + dx
                if 0 <= new_y < size and 0 <= new_x < size and garden[new_y][new_x] != '#' and not ans[new_y][new_x]:
                    new_plots.add((new_y, new_x))

        if step % 2 == 0:
            for y, x in new_plots:
                ans[y][x] = True

        plots = new_plots

    return sum(sum(row) for row in ans)


grid_width = STEPS // size - 1

odd = (grid_width // 2 * 2 + 1) ** 2
even = ((grid_width + 1) // 2 * 2) ** 2

odd_plots = fill(start_y, start_x, size * 2 + 1)
even_plots = fill(start_y, start_x, size * 2)

steps = size - 1
corners = sum((
    fill(0, start_x, steps),
    fill(size - 1, start_x, steps),
    fill(start_y, 0, steps),
    fill(start_y, size - 1, steps)
))

small_triangles, large_triangles = (
    sum((
        fill(0, 0, steps),
        fill(0, size - 1, steps),
        fill(size - 1, 0, steps),
        fill(size - 1, size - 1, steps)
    ))
    for steps in (size // 2 - 1, size * 3 // 2 - 1)
)

print(sum((
    odd * odd_plots,
    even * even_plots,
    corners,
    (grid_width + 1) * small_triangles,
    grid_width * large_triangles
)))
