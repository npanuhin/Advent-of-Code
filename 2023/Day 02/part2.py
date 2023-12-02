with open('input.txt', 'r') as file:
    games = []
    for line in filter(None, map(str.strip, file)):
        games.append([])
        for cubes in line.split(':')[1].split(';'):
            games[-1].append([])
            for cube in cubes.split(','):
                amount, name = cube.strip().split()
                games[-1][-1].append([int(amount), name])


sum_of_powers = 0

for game_num, game in enumerate(games):
    minimum = {color: 0 for color in ('red', 'green', 'blue')}
    for show in game:
        for amount, name in show:
            minimum[name] = max(minimum[name], amount)

    sum_of_powers += minimum['red'] * minimum['green'] * minimum['blue']

print(sum_of_powers)
