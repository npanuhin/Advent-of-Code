with open("input.txt", 'r', encoding="utf-8") as file:
    heightmap = [list(map(int, line.strip())) for line in file]

n, m = len(heightmap), len(heightmap[0])

visited = tuple([False] * m for _ in range(n))


def search_basin(i, j):
    if heightmap[i][j] == 9 or visited[i][j]:
        return 0

    visited[i][j] = True

    return 1 + sum((
        0 if j == 0 or heightmap[i][j] >= heightmap[i][j - 1] else search_basin(i, j - 1),      # left
        0 if i == 0 or heightmap[i][j] >= heightmap[i - 1][j] else search_basin(i - 1, j),      # up
        0 if i == n - 1 or heightmap[i][j] >= heightmap[i + 1][j] else search_basin(i + 1, j),  # right
        0 if j == m - 1 or heightmap[i][j] >= heightmap[i][j + 1] else search_basin(i, j + 1)   # down
    ))


basin_sizes = []
for i in range(n):
    for j in range(m):
        if all((
            j == 0 or heightmap[i][j] < heightmap[i][j - 1],      # left
            i == 0 or heightmap[i][j] < heightmap[i - 1][j],      # up
            i == n - 1 or heightmap[i][j] < heightmap[i + 1][j],  # right
            j == m - 1 or heightmap[i][j] < heightmap[i][j + 1]   # down
        )):
            basin_sizes.append(search_basin(i, j))

basin_sizes.sort()

print(basin_sizes.pop() * basin_sizes.pop() * basin_sizes.pop())
