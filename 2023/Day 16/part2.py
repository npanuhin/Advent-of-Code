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


with open('input.txt') as file:
    layout = [list(line) for line in filter(None, map(str.strip, file))]

width, height = len(layout[0]), len(layout)

starting_points = sum((
    [(x, -1, 'v') for x in range(width)],
    [(x, 0, '^') for x in range(width)],
    [(-1, y, '>') for y in range(height)],
    [(0, y, '<') for y in range(height)]  # 0 insted of height/width also works because of negative indexing
), [])

max_energized = 0
for start_x, start_y, direction in starting_points:

    visited = [[set() for _ in range(width)] for _ in range(height)]

    stack = [(start_x, start_y, direction)]
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

    max_energized = max(max_energized, sum(
        bool(visited[y][x])
        for y in range(height)
        for x in range(width)
    ))

print(max_energized)
