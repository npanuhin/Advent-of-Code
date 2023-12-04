with open('input.txt') as file:
    scatchcards = [
        [
            list(map(int, items))
            for items in map(str.split, line.split(':')[1].split('|'))
        ]
        for line in filter(None, map(str.strip, file))
    ]

points = 0
for winning, current in scatchcards:
    cur_points = 1
    for number in current:
        if number in winning:
            cur_points *= 2

    points += cur_points // 2

print(points)
