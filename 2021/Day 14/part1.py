from collections import defaultdict


with open("input.txt", 'r') as file:
    polymer = list(file.readline().strip())

    rules = {}
    for line in filter(lambda line: line, map(str.strip, file)):
        rule, element = map(str.strip, line.split('->'))
        rules[tuple(rule)] = element

pairs = defaultdict(int, tuple(
    ((polymer[i - 1], polymer[i]), 1)
    for i in range(1, len(polymer))
))

for step in range(10):
    old_pairs, pairs = pairs, defaultdict(int)

    for rule, element in rules.items():
        pairs[(rule[0], element)] += old_pairs[rule]
        pairs[(element, rule[1])] += old_pairs[rule]

count = defaultdict(int, {polymer[0]: 1, polymer[-1]: 1})
for pair, amount in pairs.items():
    count[pair[0]] += amount
    count[pair[1]] += amount

print((max(count.values()) - min(count.values())) // 2)
