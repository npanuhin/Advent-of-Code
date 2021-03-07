MOVES = {
    "nw": (1, -1),
    "sw": (1, 1),
    "se": (-1, 1),
    "ne": (-1, -1),
    "w": (2, 0),
    "e": (-2, 0)
}

black = set()

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        line_pos = 0
        coords = [0, 0]

        while line_pos < len(line.strip()):

            for move in MOVES:
                if line.startswith(move, line_pos):
                    coords[0] += MOVES[move][0]
                    coords[1] += MOVES[move][1]
                    line_pos += len(move)

        coords = tuple(coords)
        if coords in black:
            black.remove(coords)
        else:
            black.add(coords)

print(len(black))
