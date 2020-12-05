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


with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

field = [[place == '#' for place in line] for line in inp]

answer = 1

answer *= count(field, 1, 1)
answer *= count(field, 3, 1)
answer *= count(field, 5, 1)
answer *= count(field, 7, 1)
answer *= count(field, 1, 2)

print(answer)
