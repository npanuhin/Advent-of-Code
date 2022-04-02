from statistics import median

with open("input.txt", 'r', encoding="utf-8") as file:
    crabs = list(map(int, file.read().split(',')))

target = int(median(crabs))

print(sum(abs(crab - target) for crab in crabs))
