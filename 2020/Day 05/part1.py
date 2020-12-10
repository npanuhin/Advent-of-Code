with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

max_ID = -1

for string in inp:

    left, right = 0, 128
    for i in range(7):
        middle = (left + right) // 2

        if string[i] == 'B':
            left = middle
        else:
            right = middle

    row = left

    left, right = 0, 8
    for i in range(7, 10):
        middle = (left + right) // 2

        if string[i] == 'R':
            left = middle
        else:
            right = middle

    column = left

    ID = row * 8 + column

    max_ID = max(max_ID, ID)

print(max_ID)
