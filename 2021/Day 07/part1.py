from statistics import median

with open("input.txt", 'r') as file:
    crabs = list(map(int, file.read().split(',')))

target = int(median(crabs))

print(sum(abs(crab - target) for crab in crabs))
