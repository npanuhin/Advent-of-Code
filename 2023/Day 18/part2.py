DIRECTIONS = {
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
    'U': (-1, 0)
}
DIRECTIONS_LIST = list(DIRECTIONS.keys())

with open('input.txt') as file:
    plan = []
    for line in filter(None, map(str.strip, file)):
        _, _, color = line.split()
        direction = DIRECTIONS_LIST[int(color[-2])]
        length = int(color[2:-2], 16)
        plan.append([direction, length])

signed_area = perimeter = 0

y = x = 0
for direction, length in plan:
    perimeter += length

    dy, dx = DIRECTIONS[direction]
    new_y = y + dy * length
    new_x = x + dx * length

    signed_area += (y + new_y) * (x - new_x)

    y, x = new_y, new_x

# A total of 4 corders are not canceled out and look outwards 4 * 0.5 * 0.5
print(signed_area // 2 + perimeter // 2 + 1)
