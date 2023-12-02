answer = 0

with open("input.txt") as file:
    for line in file:
        boundaries, charecter, string = line.split()

        lowest, highest = map(int, boundaries.split('-'))
        charecter = charecter.rstrip(':')

        if (string[lowest - 1] == charecter) ^ (string[highest - 1] == charecter):
            answer += 1

print(answer)
