def find_left(line: str) -> str:
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]


def find_right(line: str) -> str:
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return line[i]


with open('input.txt') as file:
    lines = list(filter(None, map(str.strip, file)))

print(sum(
    int(find_left(line) + find_right(line))
    for line in lines
))
