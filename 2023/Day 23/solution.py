from collections import defaultdict
from sys import setrecursionlimit


setrecursionlimit(10 ** 6)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_neighbours(x: int, y: int) -> list[tuple[int, int]]:
    yield from (
        (x + dx, y + dy)
        for dy, dx in DIRECTIONS
        if 0 <= x + dx < width and 0 <= y + dy < height
    )


def part1(terrain):
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
    return find_logest_path(start_x, start_y, visited)


def part2(terrain):
    def find_intersections(x, y, prev=None, distance=0):
        if prev and sum(terrain[test_y][test_x] != '#' for test_x, test_y in get_neighbours(x, y)) > 2:
            yield ((x, y), distance)
            return

        for new_x, new_y in get_neighbours(x, y):
            if (new_x, new_y) == prev:
                continue

            if terrain[new_y][new_x] != '#':
                yield from find_intersections(new_x, new_y, (x, y), distance + 1)

    first_intersection, before_first_distance = next(find_intersections(start_x, start_y))
    last_intersection, after_last_distance = next(find_intersections(end_x, end_y))

    intesections_graph = defaultdict(dict)
    todo = [first_intersection]
    while todo:
        x, y = todo.pop()
        intesections_graph[y][x] = list(find_intersections(x, y))
        todo.extend(
            (x, y)
            for (x, y), _ in intesections_graph[y][x]
            if x not in intesections_graph.get(y, [])
        )

    def find_logest_path(x: int, y: int, visited: list[list[bool]]) -> int:
        if (x, y) == last_intersection:
            return 0

        length = float('-inf')
        visited[y][x] = True

        for (new_x, new_y), distance in intesections_graph[y][x]:
            if not visited[new_y][new_x]:
                length = max(length, find_logest_path(new_x, new_y, visited) + distance)

        visited[y][x] = False
        return length

    visited = [[False] * width for _ in range(height)]
    return before_first_distance + find_logest_path(*first_intersection, visited) + after_last_distance


with open('input.txt') as file:
    terrain = list(filter(None, map(str.strip, file)))

width, height = len(terrain[0]), len(terrain)

start_y, start_x = 0, terrain[0].index('.')
end_y, end_x = height - 1, terrain[height - 1].index('.')

print(part1(terrain))
print(part2(terrain))
