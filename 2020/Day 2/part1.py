with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

answer = 0

for line in inp:
    boundaries, charecter, string = line.split()

    lowest, highest = map(int, boundaries.split('-'))
    charecter = charecter.rstrip(':')

    if lowest <= string.count(charecter) <= highest:
        answer += 1

print(answer)
