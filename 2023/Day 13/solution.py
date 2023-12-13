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


def part1(notes):
    return sum(
        find_mirror(note, len(note[0]), len(note))
        for note in notes
    )


def part2(notes):
    answer = 0
    for note in notes:
        width, height = len(note[0]), len(note)
        cur_mirror = find_mirror(note, width, height)

        for y in range(height):
            for x in range(width):
                note[y][x] = '.' if note[y][x] == '#' else '#'

                new_mirror = find_mirror(note, width, height, cur_mirror)
                if new_mirror is not None:
                    answer += new_mirror
                    break

                note[y][x] = '.' if note[y][x] == '#' else '#'
            else:
                continue
            break

    return answer


with open('input.txt') as file:
    notes = [
        list(map(list, note.splitlines()))
        for note in file.read().split('\n\n')
    ]

print(part1(notes))
print(part2(notes))
