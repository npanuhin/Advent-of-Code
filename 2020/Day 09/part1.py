def find_first_invalid(numbers):
    for k in range(25, len(numbers)):
        if not any(
            numbers[i] + numbers[j] == numbers[k]
            for i in range(k - 25, k)
            for j in range(i + 1, k)
        ):
            return numbers[k]


with open("input.txt") as file:
    inp = list(map(int, file))

print(find_first_invalid(inp))
