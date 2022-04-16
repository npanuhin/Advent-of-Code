with open("input.txt", 'r', encoding="utf-8") as file:
    cups = list(map(int, file.readline().strip()))

carousel = list(range(1, 1_000_002))
carousel[-1] = 1
for i in range(len(cups) - 1):
    carousel[cups[i]] = cups[i + 1]
carousel[cups[-1]] = len(cups) + 1

current = cups[0]
for step in range(10_000_000):
    dest = current - 1 if current > 1 else 1_000_000

    first = carousel[current]
    second = carousel[first]
    third = carousel[second]

    while dest == first or dest == second or dest == third:
        dest = dest - 1 if dest > 1 else 1_000_000

    carousel[current] = carousel[third]
    carousel[third] = carousel[dest]
    carousel[dest] = first

    current = carousel[current]

print(carousel[1] * carousel[carousel[1]])
