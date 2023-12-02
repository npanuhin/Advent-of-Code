with open("input.txt") as file:
    card = int(file.readline())
    door = int(file.readline())

i = 0
n = 1
while n != card:
    n = (n * 7) % 20201227
    i += 1

print(pow(door, i, 20201227))
