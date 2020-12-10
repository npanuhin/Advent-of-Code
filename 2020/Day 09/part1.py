from collections import deque


def find_first_invalid(numbers):
    d = deque(numbers[i] for i in range(25))

    for k in range(25, len(numbers)):

        if not any(
            numbers[i] + numbers[j] == numbers[k]
            for i in range(k - 25, k)
            for j in range(k - 25, k)
        ):
            return numbers[k]

        d.append(numbers[k])
        d.popleft()


with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(int, file.readlines()))

print(find_first_invalid(inp))
