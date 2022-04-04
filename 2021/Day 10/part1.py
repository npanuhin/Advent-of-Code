character_match = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

illegal_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

with open("input.txt", 'r') as file:
    lines = [line.strip() for line in file]

answer = 0

for line in lines:
    stack = []
    for item in line:
        if item in ('(', '[', '{', '<'):
            stack.append(item)
        elif item != character_match[stack.pop()]:
            answer += illegal_points[item]
            break

print(answer)
