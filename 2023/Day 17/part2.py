from heapq import heappush, heappop


def traverse(city):
    width, height = len(city[0]), len(city)

    seen = set()

    queue = []
    heappush(queue, (0, 0, 0, False))
    heappush(queue, (0, 0, 0, True))

    while queue:
        cost, x, y, axis = heappop(queue)

        if x == width - 1 and y == height - 1:
            return cost

        if (x, y, axis) in seen:
            continue
        seen.add((x, y, axis))

        for direction in (-1, 1):
            new_y, new_x = y, x
            add_cost = 0

            for distance in range(1, 11):
                if axis:
                    new_x += direction
                    if not 0 <= new_x < width:
                        break
                else:
                    new_y += direction
                    if not 0 <= new_y < height:
                        break

                add_cost += city[new_y][new_x]

                if distance >= 4:
                    heappush(queue, (cost + add_cost, new_x, new_y, not axis))


with open('input.txt') as file:
    city = [list(map(int, line)) for line in filter(None, map(str.strip, file))]

print(traverse(city))
