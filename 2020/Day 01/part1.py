with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(int, file.readlines()))

inp.sort()

for i in range(len(inp) - 1):

    left, right = i + 1, len(inp)
    while right - left > 1:
        middle = (left + right) // 2

        if inp[middle] <= 2020 - inp[i]:
            left = middle
        else:
            right = middle

    if inp[i] + inp[left] == 2020 and left != i:
        print(inp[i] * inp[left])
