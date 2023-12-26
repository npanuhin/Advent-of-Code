from sys import setrecursionlimit


setrecursionlimit(10 ** 6)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


with open('input.txt') as file:
    terrain = list(filter(None, map(str.strip, file)))

width, height = len(terrain[0]), len(terrain)

start_y, start_x = 0, terrain[0].index('.')


def find_logest_path(x: int, y: int, visited: list[list[bool]]) -> int:
    if y == height - 1:
        return 0

    length = float('-inf')

    visited[y][x] = True

    for dy, dx in DIRECTIONS:
        if not (0 <= x + dx < width and 0 <= y + dy < height) or visited[y + dy][x + dx]:
            continue

        if any((
            terrain[y + dy][x + dx] == '.',
            terrain[y + dy][x + dx] == '>' and dx == 1,
            terrain[y + dy][x + dx] == '<' and dx == -1,
            terrain[y + dy][x + dx] == '^' and dy == -1,
            terrain[y + dy][x + dx] == 'v' and dy == 1
        )):
            length = max(length, find_logest_path(x + dx, y + dy, visited))

    visited[y][x] = False

    return length + 1


visited = [[False] * width for _ in range(height)]
print(find_logest_path(start_x, start_y, visited))
