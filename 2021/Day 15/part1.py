from heapq import heapify, heappush, heappop


MOVES = ((0, 1), (0, -1), (1, 0), (-1, 0))

with open("input.txt", 'r') as file:
    cavern = [list(map(int, line)) for line in map(str.strip, file) if line]

size_y, size_x = len(cavern), len(cavern[0])

costs = [[None] * size_x for _ in range(size_y)]

pqueue = [(0, 0, 0)]
heapify(pqueue)

while pqueue:
    cost, row, col = heappop(pqueue)
    if costs[row][col] is not None:
        continue

    costs[row][col] = cost

    if row == size_y - 1 and col == size_x - 1:
        break

    for dy, dx in MOVES:
        new_row = row + dy
        new_col = col + dx
        if not (0 <= new_row < size_y and 0 <= new_col < size_x):
            continue

        heappush(pqueue, (cost + cavern[new_row][new_col], new_row, new_col))

print(costs[-1][-1])
