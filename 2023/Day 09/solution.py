def extrapolate(history: list[int]) -> int:
    if all(item == 0 for item in history):
        return 0

    differences = []
    for i in range(len(history) - 1):
        differences.append(history[i + 1] - history[i])

    return history[-1] + extrapolate(differences)


def part1(histories):
    return sum(map(extrapolate, histories))


def part2(histories):
    histories = [list(reversed(history)) for history in histories]
    return sum(map(extrapolate, histories))


with open('input.txt') as file:
    histories = [
        list(map(int, line.split()))
        for line in filter(None, map(str.strip, file))
    ]

print(part1(histories))
print(part2(histories))
