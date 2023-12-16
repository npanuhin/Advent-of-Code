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

visited = [[set() for _ in range(width)] for _ in range(height)]

stack = [(-1, 0, '>')]
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

print(sum(
    bool(visited[y][x])
    for y in range(height)
    for x in range(width)
))
