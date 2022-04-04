with open("input.txt", 'r') as file:
    octopuses = [list(map(int, line.strip())) for line in file]

n = len(octopuses)


def ignite(i, j):
    octopuses[i][j] += 1
    if octopuses[i][j] <= 9:
        return 0

    octopuses[i][j] = float("-inf")

    return 1 + sum(
        ignite(new_i, new_j)
        for new_i in range(max(0, i - 1), min(n, i + 2))
        for new_j in range(max(0, j - 1), min(n, j + 2))
    )


flashes = 0

for step in range(100):
    for i in range(n):
        for j in range(n):
            flashes += ignite(i, j)

    for i in range(n):
        for j in range(n):
            if octopuses[i][j] == float("-inf"):
                octopuses[i][j] = 0

print(flashes)
