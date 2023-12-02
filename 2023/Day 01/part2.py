DIGIT_NAMES = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def find_left(line: str) -> str:
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]

        for name, value in DIGIT_NAMES.items():
            if line[i:i + len(name)] == name:
                return str(value)


def find_right(line: str) -> str:
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return line[i]

        for name, value in DIGIT_NAMES.items():
            if line[i - len(name) + 1:i + 1] == name:
                return str(value)


with open('input.txt') as file:
    lines = list(filter(None, map(str.strip, file)))

print(sum(
    int(find_left(line) + find_right(line))
    for line in lines
))
