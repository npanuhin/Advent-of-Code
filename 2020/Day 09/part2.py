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

invalid_num = find_first_invalid(inp)

range_end = -1
summ = 0
for range_start in range(len(inp)):
    while summ < invalid_num:
        range_end += 1
        summ += inp[range_end]

    if summ == invalid_num and range_start != range_end:
        print(
            min(inp[i] for i in range(range_start, range_end + 1)) +
            max(inp[i] for i in range(range_start, range_end + 1))
        )

    summ -= inp[range_start]
