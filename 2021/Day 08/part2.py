answer = 0

with open("input.txt") as file:
    for line in file:
        digit_map = {}
        patterns, output = (
            list(map(frozenset, item.split()))
            for item in line.split('|')
        )

        for pattern in patterns:
            if len(pattern) == 2:
                digit_map[1] = pattern
            elif len(pattern) == 4:
                digit_map[4] = pattern
            elif len(pattern) == 3:
                digit_map[7] = pattern
            elif len(pattern) == 7:
                digit_map[8] = pattern

        for pattern in patterns:
            if len(pattern) == 6:
                if digit_map[4].issubset(pattern):
                    digit_map[9] = pattern
                elif digit_map[1].issubset(pattern):
                    digit_map[0] = pattern
                else:
                    digit_map[6] = pattern

        for pattern in patterns:
            if len(pattern) == 5:
                if pattern.issubset(digit_map[6]):
                    digit_map[5] = pattern
                elif digit_map[1].issubset(pattern):
                    digit_map[3] = pattern
                else:
                    digit_map[2] = pattern

        digit_reverse_map = {value: key for key, value in digit_map.items()}

        for i, digit in enumerate(output):
            answer += digit_reverse_map[digit] * (10 ** (len(output) - i - 1))

print(answer)
