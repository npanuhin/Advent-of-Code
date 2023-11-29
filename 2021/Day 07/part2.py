from math import floor, ceil


def calc(target):
    return sum(d * (d + 1) // 2 for d in (abs(crab - target) for crab in crabs))


with open("input.txt", 'r') as file:
    crabs = list(map(int, file.read().split(',')))

mean = sum(crabs) / len(crabs)

print(min(
    calc(floor(mean)),
    calc(ceil(mean))
))
