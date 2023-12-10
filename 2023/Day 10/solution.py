# Unfortunatly, not a traditional part1()/part2() code structure

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
left, right = [], []
area = 0
distance = 0

while cur_x != start_x or cur_y != start_y or grid[cur_y][cur_x]:
    tmp_cur_x, tmp_cur_y = cur_x, cur_y
    distance += 1

    match grid[cur_y][cur_x]:
        case '|':
            if last_y == cur_y - 1:
                right.append((cur_x - 1, cur_y))
                left.append((cur_x + 1, cur_y))
                cur_y += 1  # Down
            else:
                right.append((cur_x + 1, cur_y))
                left.append((cur_x - 1, cur_y))
                cur_y -= 1  # Up

        case '-':
            if last_x == cur_x - 1:
                left.append((cur_x, cur_y - 1))
                right.append((cur_x, cur_y + 1))
                cur_x += 1  # Right
            else:
                right.append((cur_x, cur_y - 1))
                left.append((cur_x, cur_y + 1))
                cur_x -= 1  # Left

        case '7':
            if last_x == cur_x - 1:
                left.append((cur_x, cur_y - 1))
                left.append((cur_x + 1, cur_y))
                cur_y += 1  # Down
            else:
                right.append((cur_x, cur_y - 1))
                right.append((cur_x + 1, cur_y))
                cur_x -= 1  # Left

        case 'J':
            if last_y == cur_y - 1:
                left.append((cur_x + 1, cur_y))
                left.append((cur_x, cur_y + 1))
                cur_x -= 1  # Left
            else:
                right.append((cur_x + 1, cur_y))
                right.append((cur_x, cur_y + 1))
                cur_y -= 1  # Up

        case 'L':
            if last_y == cur_y - 1:
                right.append((cur_x - 1, cur_y))
                right.append((cur_x, cur_y + 1))
                cur_x += 1  # Right
            else:
                left.append((cur_x - 1, cur_y))
                left.append((cur_x, cur_y + 1))
                cur_y -= 1  # Up

        case 'F':
            if last_x == cur_x + 1:
                right.append((cur_x, cur_y - 1))
                right.append((cur_x - 1, cur_y))
                cur_y += 1  # Down
            else:
                left.append((cur_x, cur_y - 1))
                left.append((cur_x - 1, cur_y))
                cur_x += 1  # Right

    last_x, last_y = tmp_cur_x, tmp_cur_y
    grid[last_y][last_x] = None
    area += (cur_x - last_x) * cur_y  # If vertical movement: 0


# Part 1
print(distance // 2)

# Part 2
count = 0
stack = left if area >= 0 else right  # If area < 0: clockwise; else: counter-clockwise
while stack:
    x, y = stack.pop()

    if not 0 <= x < width or not 0 <= y < height or grid[y][x] is None:
        continue

    grid[y][x] = None
    count += 1

    for new_x in range(x - 1, x + 2):
        for new_y in range(y - 1, y + 2):
            stack.append((new_x, new_y))

print(count)
