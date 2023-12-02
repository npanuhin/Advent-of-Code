TOTAL_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('input.txt') as file:
    games = []
    for line in filter(None, map(str.strip, file)):
        games.append([])
        for cubes in line.split(':')[1].split(';'):
            games[-1].append([])
            for cube in cubes.split(','):
                amount, name = cube.strip().split()
                games[-1][-1].append([int(amount), name])


sum_of_possible = 0

for game_num, game in enumerate(games):
    if all(
        amount <= TOTAL_CUBES[name]
        for show in game
        for amount, name in show
    ):
        sum_of_possible += game_num + 1

print(sum_of_possible)
