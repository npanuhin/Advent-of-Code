data = [set()]

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        if not line.strip():
            data.append(set())
        else:
            data[-1] |= set(line.strip())

print(sum(len(group) for group in data))
