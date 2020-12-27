from collections import defaultdict


with open("input.txt", 'r', encoding="utf-8") as file:
    adapters = list(map(int, file.readlines()))

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1] + 3)

ways = defaultdict(lambda: 0, {0: 1})

for adapter in adapters:
    for parent_adapter in range(adapter - 3, adapter):
        ways[adapter] += ways[parent_adapter]

print(ways[adapters[-1]])
