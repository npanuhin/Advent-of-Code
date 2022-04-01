from collections import deque

answer = 0

with open("input.txt", 'r') as file:
    window = deque(int(file.readline()) for _ in range(3))
    prev = sum(window)
    for line in file:
        window.popleft()
        window.append(int(line))
        cur = sum(window)
        if prev < cur:
            answer += 1
        prev = cur


print(answer)
