with open("input.txt", 'r', encoding="utf-8") as file:
    heightmap = [list(map(int, line.strip())) for line in file]

n, m = len(heightmap), len(heightmap[0])
answer = 0

for i in range(n):
    for j in range(m):
        if all((
            j == 0 or heightmap[i][j] < heightmap[i][j - 1],      # left
            i == 0 or heightmap[i][j] < heightmap[i - 1][j],      # up
            i == n - 1 or heightmap[i][j] < heightmap[i + 1][j],  # right
            j == m - 1 or heightmap[i][j] < heightmap[i][j + 1]   # down
        )):
            answer += heightmap[i][j] + 1

print(answer)
