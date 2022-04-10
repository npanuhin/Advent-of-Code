from collections import deque


count = deque(0 for _ in range(9))

with open("input.txt", 'r') as file:
    for item in map(int, file.read().split(',')):
        count[item] += 1

for day in range(256):
    count[7] += count[0]
    count.append(count.popleft())

print(sum(count))
