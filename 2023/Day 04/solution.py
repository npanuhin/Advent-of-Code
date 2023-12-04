def part1(scatchcards):
    points = 0
    for winning, current in scatchcards:
        cur_points = 1
        for number in current:
            if number in winning:
                cur_points *= 2

        points += cur_points // 2

    return points


def part2(scatchcards):
    copies = [1] * len(scatchcards)

    for i, (winning, current) in enumerate(scatchcards):
        cur_winning = sum(
            number in winning
            for number in current
        )

        for j in range(cur_winning):
            copies[i + j + 1] += copies[i]

    return sum(copies)


with open('input.txt') as file:
    scatchcards = [
        [
            list(map(int, items))
            for items in map(str.split, line.split(':')[1].split('|'))
        ]
        for line in filter(None, map(str.strip, file))
    ]

print(part1(scatchcards))
print(part2(scatchcards))
