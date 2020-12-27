from string import ascii_letters


data = [set(ascii_letters)]

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        if not line.strip():
            data.append(set(ascii_letters))
        else:
            data[-1] = data[-1].intersection(line.strip())

print(sum(len(group) for group in data))
