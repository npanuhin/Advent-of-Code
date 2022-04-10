character_match = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

completion_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

with open("input.txt", 'r') as file:
    lines = [line.strip() for line in file]

scores = []

for line in lines:
    stack = []
    score = 0
    for item in line:
        if item in ('(', '[', '{', '<'):
            stack.append(item)
        elif item != character_match[stack.pop()]:
            break

    else:
        while stack:
            score *= 5
            score += completion_points[character_match[stack.pop()]]

        scores.append(score)

print(sorted(scores)[len(scores) // 2])
