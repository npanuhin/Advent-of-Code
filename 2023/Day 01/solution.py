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


def find_left(line: str, check_names: bool) -> str:
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]

        if check_names:
            for name, value in DIGIT_NAMES.items():
                if line[i:i + len(name)] == name:
                    return str(value)


def find_right(line: str, check_names: bool) -> str:
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return line[i]

        if check_names:
            for name, value in DIGIT_NAMES.items():
                if line[i - len(name) + 1:i + 1] == name:
                    return str(value)


def left_right_sum(check_names=False):
    return sum(
        int(find_left(line, check_names) + find_right(line, check_names))
        for line in lines
    )


def part1(lines):
    return left_right_sum()


def part2(lines):
    return left_right_sum(True)


with open('input.txt') as file:
    lines = list(filter(None, map(str.strip, file)))

print(part1(lines))
print(part2(lines))
