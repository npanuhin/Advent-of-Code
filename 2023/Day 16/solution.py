BOUNCES = {
    '/': {
        '>': '^',
        '<': 'v',
        '^': '>',
        'v': '<'
    },
    '\\': {
        '>': 'v',
        '<': '^',
        '^': '<',
        'v': '>'
    },
    '|': {
        '>': 'v^',
        '<': 'v^',
        '^': '^',
        'v': 'v'
    },
    '-': {
        '>': '>',
        '<': '<',
        '^': '<>',
        'v': '<>'
    }
}


def calc(layout, start_x: int, start_y: int, start_direction: str):
    width, height = len(layout[0]), len(layout)

    visited = [[set() for _ in range(width)] for _ in range(height)]

    stack = [(start_x, start_y, start_direction)]
    while stack:
        x, y, direction = stack.pop()

        match direction:
            case '<':
                x -= 1
            case '>':
                x += 1
            case '^':
                y -= 1
            case 'v':
                y += 1

        if not 0 <= x < width or not 0 <= y < height or direction in visited[y][x]:
            continue

        visited[y][x].add(direction)

        if layout[y][x] == '.':
            stack.append((x, y, direction))
        else:
            for new_direction in BOUNCES[layout[y][x]][direction]:
                stack.append((x, y, new_direction))

    return sum(
        bool(visited[y][x])
        for y in range(height)
        for x in range(width)
    )


def part1(layout):
    return calc(layout, -1, 0, '>')


def part2(layout):
    starting_points = sum((
        [(x, -1, 'v') for x in range(len(layout[0]))],
        [(x, 0, '^') for x in range(len(layout[0]))],
        [(-1, y, '>') for y in range(len(layout))],
        [(0, y, '<') for y in range(len(layout))]  # 0 insted of height/width also works because of negative indexing
    ), [])

    return max(calc(layout, *point) for point in starting_points)


with open('input.txt') as file:
    layout = tuple(filter(None, map(str.strip, file)))

print(part1(layout))
print(part2(layout))
