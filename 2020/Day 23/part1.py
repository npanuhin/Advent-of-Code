with open("input.txt") as file:
    cups = list(map(int, file.readline().strip()))

carousel = [None] * (len(cups) + 1)
carousel[-1] = 1
for i in range(len(cups) - 1):
    carousel[cups[i]] = cups[i + 1]
carousel[cups[-1]] = 1

current = cups[0]
for step in range(100):
    dest = current - 1 if current > 1 else 9

    first = carousel[current]
    second = carousel[first]
    third = carousel[second]

    while dest in (first, second, third):
        dest = dest - 1 if dest > 1 else 9

    carousel[current] = carousel[third]
    carousel[third] = carousel[dest]
    carousel[dest] = first

    current = carousel[current]

labels = [carousel[1]]
while labels[-1] != 1:
    labels.append(carousel[labels[-1]])

print("".join(map(str, labels[:-1])))
