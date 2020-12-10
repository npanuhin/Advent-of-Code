from string import ascii_letters

with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

data = [set(ascii_letters)]

for line in inp:
    if not line:
        data.append(set(ascii_letters))
    else:
        data[-1] = data[-1].intersection(line)

print(sum(len(group) for group in data))
