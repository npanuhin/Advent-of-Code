from collections import defaultdict, deque
from itertools import chain as iterator_chain

DIRECTIONS = deque([(0, -1), (1, 0), (0, 1), (-1, 0)])


def build_sea_borders(sea, used, x, y):
    cur_tileid = sea[y][x]
    used[cur_tileid] = True

    if len(neighbors[cur_tileid]) == 2:
        DIRECTIONS.append(DIRECTIONS.popleft())

    for neighbor in neighbors[cur_tileid]:
        if not used[neighbor] and len(neighbors[neighbor]) < 4:

            dy, dx = DIRECTIONS[0]
            y += dy
            x += dx

            if len(sea) <= y:
                sea.append([None] * len(sea[0]))

            if len(sea[0]) <= x:
                for line in sea:
                    line.append(None)

            sea[y][x] = neighbor
            build_sea_borders(sea, used, x, y)
            return


tiles = {}
edges = {}
tile = []
tileid = None

with open("input.txt") as file:
    for line in iterator_chain(file, [""]):
        line = line.strip()

        if not line:
            if tile:
                tilesize = len(tile)
                tiles[tileid] = tile
                edges[tileid] = set((
                    tile[0], tile[0][::-1],
                    tile[-1], tile[-1][::-1],
                    "".join(line[0] for line in tile), "".join(line[0] for line in tile)[::-1],
                    "".join(line[-1] for line in tile), "".join(line[-1] for line in tile)[::-1]
                ))

            tile = []

        elif line.startswith("Tile"):
            tileid = int(line.lstrip("Tile").rstrip(':'))

        else:
            tile.append(line)


neighbors = defaultdict(set)
for tileid1, edges1 in edges.items():
    for tileid2, edges2 in edges.items():

        if tileid1 == tileid2:
            continue

        if edges1 & edges2:
            neighbors[tileid1].add(tileid2)
            neighbors[tileid2].add(tileid1)

used = {tileid: False for tileid in edges}
sea = [[next(tile for tile, neighbor_edges in neighbors.items() if len(neighbor_edges) == 2)]]

build_sea_borders(sea, used, 0, 0)

sea_height, sea_width = len(sea), len(sea[0])

for y in range(1, sea_height - 1):
    for x in range(1, sea_width - 1):
        sea[y][x] = next(tileid
                         for tileid in neighbors[sea[y][x - 1]] & neighbors[sea[y - 1][x]]
                         if not used[tileid]
                         )
        used[sea[y][x]] = True

print(sea[0][0] * sea[0][sea_width - 1] * sea[sea_height - 1][0] * sea[sea_height - 1][sea_width - 1])
