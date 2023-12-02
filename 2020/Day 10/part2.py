from collections import defaultdict


with open("input.txt") as file:
    adapters = sorted(list(map(int, file)) + [0])

adapters.append(adapters[-1] + 3)

ways = defaultdict(lambda: 0, {0: 1})

for adapter in adapters:
    for parent_adapter in range(adapter - 3, adapter):
        ways[adapter] += ways[parent_adapter]

print(ways[adapters[-1]])
