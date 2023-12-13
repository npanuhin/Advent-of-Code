def find_mirror(note: str, width: int, height: int, discard_result=None) -> int | None:
    # Find vertical mirroring
    for x in range(1, width):
        if x == discard_result:
            continue

        if all(
            note[y][x - i - 1] == note[y][x + i]
            for y in range(height)
            for i in range(min(x, width - x))
        ):
            return x

    # Find horizontal mirroring
    for y in range(1, height):
        if y * 100 == discard_result:
            continue

        if all(
            note[y - i - 1][x] == note[y + i][x]
            for x in range(width)
            for i in range(min(y, height - y))
        ):
            return y * 100


with open('input.txt') as file:
    notes = list(map(str.splitlines, file.read().split('\n\n')))

print(sum(
    find_mirror(note, len(note[0]), len(note))
    for note in notes
))
