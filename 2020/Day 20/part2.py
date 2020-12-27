from collections import defaultdict, deque
from itertools import chain as iterator_chain

DIRECTIONS = deque([(0, -1), (1, 0), (0, 1), (-1, 0)])


def rotate(image):
    return [
        "".join(image[x][y] for x in range(len(image[0])))
        for y in range(len(image))
    ]


def get_transformations(tile):
    transformations = []
    for _ in range(4):
        transformations.append(tile)
        transformations.append(tile[::-1])
        transformations.append([line[::-1] for line in tile])
        transformations.append([line[::-1] for line in tile][::-1])
        tile = rotate(tile)

    return transformations


def transform_tofit_left(tile, left_border):
    for tile in get_transformations(tile):
        if "".join(line[0] for line in tile) == left_border:
            return tile
    return None


def transform_tofit_top(tile, top_border):
    for tile in get_transformations(tile):
        if tile[0] == top_border:
            return tile
    return None


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

with open("input.txt", 'r', encoding="utf-8") as file:
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


# -------------|  This is where part 1 ends  |--------------


posible_first_tiles = get_transformations(tiles[sea[0][0]])

for first_tile in posible_first_tiles:
    sea_tiles = [[None] * sea_width for _ in range(sea_height)]
    sea_tiles[0][0] = first_tile
    valid = True

    for x in range(1, sea_width):
        sea_tiles[0][x] = transform_tofit_left(
            tiles[sea[0][x]],
            left_border="".join(line[-1] for line in sea_tiles[0][x - 1])
        )
        if sea_tiles[0][x] is None:
            valid = False
            break

    if valid:
        for y in range(1, sea_height):
            for x in range(sea_width):
                sea_tiles[y][x] = transform_tofit_top(
                    tiles[sea[y][x]],
                    top_border=sea_tiles[y - 1][x][-1]
                )
                if sea_tiles[y][x] is None:
                    valid = False
                    break
            else:
                continue
            break

        else:
            break

# Removing borders:
sea_tiles = [
    [[line[1:-1] for line in sea_tiles[y][x][1:-1]] for x in range(sea_width)]
    for y in range(sea_height)
]
tilesize -= 2

# Building image:
image = []
cur_y = 0
for y in range(sea_height):
    image += [""] * tilesize
    for x in range(sea_width):
        for tile_y in range(tilesize):
            image[cur_y + tile_y] += sea_tiles[y][x][tile_y]

    cur_y += tilesize

# Searching for sea monsters:
with open("sea_monster.txt", 'r', encoding="utf-8") as file:
    sea_monster = [line.strip('\n') for line in file]

for image in get_transformations(image):
    free = [[image[y][x] == '#' for x in range(len(image[0]))] for y in range(len(image))]
    count = 0

    for y in range(len(image) - len(sea_monster)):
        for x in range(len(image[0]) - len(sea_monster[0])):
            for dy in range(len(sea_monster)):
                for dx in range(len(sea_monster[0])):
                    if sea_monster[dy][dx] == '#' and image[y + dy][x + dx] != '#':
                        break
                else:
                    continue
                break
            else:
                count += 1
                for dy in range(len(sea_monster)):
                    for dx in range(len(sea_monster[0])):
                        if sea_monster[dy][dx] == '#':
                            free[y + dy][x + dx] = False

    if count > 0:
        print(sum(sum(item for item in line) for line in free))
        break
