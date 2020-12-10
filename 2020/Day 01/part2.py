with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(int, file.readlines()))

inp.sort()

for i in range(len(inp)):
    for j in range(i + 1, len(inp)):

        left, right = 0, len(inp)
        while right - left > 1:
            middle = (left + right) // 2

            if inp[middle] <= 2020 - inp[i] - inp[j]:
                left = middle
            else:
                right = middle

        if inp[i] + inp[j] + inp[left] == 2020 and left != i and left != j:
            print(inp[i] * inp[j] * inp[left])
