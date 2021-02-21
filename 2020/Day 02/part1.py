answer = 0

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        boundaries, charecter, string = line.split()

        lowest, highest = map(int, boundaries.split('-'))
        charecter = charecter.rstrip(':')

        if lowest <= string.count(charecter) <= highest:
            answer += 1

print(answer)
