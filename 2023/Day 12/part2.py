from functools import cache


@cache
def count_arrangements(springs, groups):
    springs = springs.lstrip('.')

    if not springs:
        return not groups

    if not groups:
        return all(spring != '#' for spring in springs)

    if springs[0] == '#':  # We are at the end of some group
        group_size = groups[0]
        if group_size > len(springs):
            return 0

        if any(springs[i] == '.' for i in range(group_size)):
            return 0

        if len(springs) > group_size and springs[group_size] == '#':
            return 0

        return count_arrangements(springs[group_size + 1:], groups[1:])

    return count_arrangements('#' + springs[1:], groups) + count_arrangements(springs[1:], groups)


with open('input.txt') as file:
    records = [
        [springs, tuple(map(int, groups.split(',')))]
        for springs, groups in (
            line.split(' ', 1)
            for line in filter(None, map(str.strip, file))
        )
    ]

records = [
    [
        ((row + '?') * 5)[:-1],
        groups * 5
    ]
    for row, groups in records
]

print(sum(
    count_arrangements(springs, groups)
    for springs, groups in records
))
