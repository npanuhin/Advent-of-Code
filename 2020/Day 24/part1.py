from collections import Counter


MOVES = {
    "nw": (1, -1),
    "sw": (1, 1),
    "se": (-1, 1),
    "ne": (-1, -1),
    "w": (2, 0),
    "e": (-2, 0)
}


def neighors(x, y):
    for dx, dy in MOVES.values():
        yield x + dx, y + dy


with open("input.txt") as file:
    flipped = []
    for line in map(str.strip, file):
        pos = x = y = 0
        while pos < len(line):
            for move, delta in MOVES.items():
                if line.startswith(move, pos):
                    x += delta[0]
                    y += delta[1]
                    pos += len(move)
                    break

        flipped.append((x, y))

print(sum(1 for count in Counter(flipped).values() if count % 2 == 1))
