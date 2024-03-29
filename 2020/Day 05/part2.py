IDs = []

with open("input.txt") as file:
    for string in file:
        string = string.strip()

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

        IDs.append(row * 8 + column)

IDs.sort()

for i in range(len(IDs)):
    if IDs[i] != IDs[0] + i:
        print(IDs[i] - 1)
        break
