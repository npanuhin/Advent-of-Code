answer = 0

with open("input.txt", 'r') as file:
    prev = file.readline()
    for cur in file:
        if int(prev) < int(cur):
            answer += 1
        prev = cur

print(answer)
