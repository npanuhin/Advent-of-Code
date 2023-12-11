with open('input.txt') as file:
    image = [list(line) for line in filter(None, map(str.strip, file))]

galaxies = [
    [y, x]
    for y in range(len(image))
    for x in range(len(image[y]))
    if image[y][x] == '#'
]

# Expand y
y_addition = [0] * len(image)
y = 0
while y < len(image):
    if all(item == '.' for item in image[y]):
        y_addition[y] = 1_000_000 - 1
    y += 1

for i in range(1, len(y_addition)):  # Prefix sum in-place
    y_addition[i] += y_addition[i - 1]

# Expand x
x_addition = [0] * len(image[0])
x = 0
while x < len(image[0]):
    if all(line[x] == '.' for line in image):
        x_addition[x] = 1_000_000 - 1
    x += 1

for i in range(1, len(x_addition)):  # Prefix sum in-place
    x_addition[i] += x_addition[i - 1]

# Apply expansion
for galaxy in galaxies:
    galaxy[0] += y_addition[galaxy[0]]
    galaxy[1] += x_addition[galaxy[1]]

# Calculate lengths
path_summ = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        x1, y1 = galaxies[i]
        x2, y2 = galaxies[j]
        path_summ += abs(x1 - x2) + abs(y1 - y2)

print(path_summ)
