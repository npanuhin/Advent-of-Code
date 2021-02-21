with open("input.txt", 'r', encoding="utf-8") as file:
    inp = sorted(map(int, file))

for i in range(len(inp) - 2):

    if inp[i] * 3 >= 2020:
        break

    for j in range(i + 1, len(inp) - 1):

        if inp[i] + inp[j] * 2 >= 2020:
            break

        left, right = j + 1, len(inp)
        while right - left > 1:
            middle = (left + right) // 2

            if inp[middle] <= 2020 - inp[i] - inp[j]:
                left = middle
            else:
                right = middle

        if inp[i] + inp[j] + inp[left] == 2020 and left != i and left != j:
            print(inp[i] * inp[j] * inp[left])
