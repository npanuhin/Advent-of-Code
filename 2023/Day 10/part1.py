PIPES = {
    '|': ['up', 'down'],
    '-': ['left', 'right'],
    '7': ['down', 'left'],
    'J': ['up', 'left'],
    'L': ['up', 'right'],
    'F': ['down', 'right']
}
PIPES_BY_DIRECTION = {
    direction: [pipe for pipe, directions in PIPES.items() if direction in directions]
    for direction in ('up', 'down', 'left', 'right')
}


with open('input.txt') as file:
    grid = [list(line) for line in filter(None, map(str.strip, file))]

width, height = len(grid[0]), len(grid)

start_x, start_y = next(
    (x, y)
    for y in range(height)
    for x in range(width)
    if grid[y][x] == 'S'
)

start_directions = []
if grid[start_y - 1][start_x] in PIPES_BY_DIRECTION['down']:
    start_directions.append('up')
if grid[start_y + 1][start_x] in PIPES_BY_DIRECTION['up']:
    start_directions.append('down')
if grid[start_y][start_x - 1] in PIPES_BY_DIRECTION['right']:
    start_directions.append('left')
if grid[start_y][start_x + 1] in PIPES_BY_DIRECTION['left']:
    start_directions.append('right')

grid[start_y][start_x] = next(pipe for pipe, directions in PIPES.items() if directions == start_directions)

last_x, last_y = cur_x, cur_y = start_x, start_y
distance = 0

while cur_x != start_x or cur_y != start_y or (last_x == start_x and last_y == start_y):
    tmp_cur_x, tmp_cur_y = cur_x, cur_y
    distance += 1

    match grid[cur_y][cur_x]:
        case '|':
            if last_y == cur_y - 1:
                cur_y += 1
            else:
                cur_y -= 1

        case '-':
            if last_x == cur_x - 1:
                cur_x += 1
            else:
                cur_x -= 1

        case '7':
            if last_x == cur_x - 1:
                cur_y += 1
            else:
                cur_x -= 1

        case 'J':
            if last_y == cur_y - 1:
                cur_x -= 1
            else:
                cur_y -= 1

        case 'L':
            if last_y == cur_y - 1:
                cur_x += 1
            else:
                cur_y -= 1

        case 'F':
            if last_x == cur_x + 1:
                cur_y += 1
            else:
                cur_x += 1

    last_x, last_y = tmp_cur_x, tmp_cur_y

print(distance // 2)
