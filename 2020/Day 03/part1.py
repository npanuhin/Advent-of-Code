def count(field, dx, dy):
    n = len(field)
    m = len(field[0])

    result = 0

    y, x = 0, 0
    while y < n:
        result += field[y][x % m]
        y += dy
        x += dx

    return result


with open("input.txt") as file:
    # Converting input to a two-dimensional bool array
    field = [[place == '#' for place in line.strip()] for line in file]

print(count(field, 3, 1))
