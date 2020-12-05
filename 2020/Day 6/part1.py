with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

data = [set()]

for line in inp:
    if not line:
        data.append(set())
    else:
        data[-1] = data[-1].union(line)

print(
    sum(len(group) for group in data)
)
