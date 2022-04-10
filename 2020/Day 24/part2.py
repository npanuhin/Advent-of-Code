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


with open("input.txt", 'r', encoding="utf-8") as file:
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


black = set(pos for pos, count in Counter(flipped).items() if count % 2 == 1)

for _ in range(100):
    black = set(
        pos
        for pos, count in Counter(
            neighor_pos
            for pos in black
            for neighor_pos in neighors(*pos)
        ).items()
        if count == 2 or (count == 1 and pos in black)
    )

print(len(black))
