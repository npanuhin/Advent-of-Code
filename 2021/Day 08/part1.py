answer = 0

with open("input.txt") as file:
    for line in file:
        patterns, output = (
            list(map(frozenset, item.split()))
            for item in line.split('|')
        )

        for pattern in output:
            if len(pattern) in (2, 3, 4, 7):
                answer += 1

print(answer)
