TOTAL_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def part1(games):
    sum_of_possible = 0

    for game_num, game in enumerate(games):
        if all(
            amount <= TOTAL_CUBES[name]
            for show in game
            for amount, name in show
        ):
            sum_of_possible += game_num + 1

    return sum_of_possible


def part2(games):
    sum_of_powers = 0

    for game_num, game in enumerate(games):
        minimum = {color: 0 for color in ('red', 'green', 'blue')}
        for show in game:
            for amount, name in show:
                minimum[name] = max(minimum[name], amount)

        sum_of_powers += minimum['red'] * minimum['green'] * minimum['blue']

    return sum_of_powers


with open('input.txt') as file:
    games = []
    for line in filter(None, map(str.strip, file)):
        games.append([])
        for cubes in line.split(':')[1].split(';'):
            games[-1].append([])
            for cube in cubes.split(','):
                amount, name = cube.strip().split()
                games[-1][-1].append([int(amount), name])

print(part1(games))
print(part2(games))
