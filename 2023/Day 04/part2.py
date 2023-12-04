with open('input.txt') as file:
    scatchcards = [
        [
            list(map(int, items))
            for items in map(str.split, line.split(':')[1].split('|'))
        ]
        for line in filter(None, map(str.strip, file))
    ]

copies = [1] * len(scatchcards)

for i, (winning, current) in enumerate(scatchcards):
    cur_winning = sum(
        number in winning
        for number in current
    )

    for j in range(cur_winning):
        copies[i + j + 1] += copies[i]

print(sum(copies))
