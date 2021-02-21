with open("input.txt", 'r', encoding="utf-8") as file:
    adapters = sorted(list(map(int, file)) + [0])

jolt_diff = [0, 0, 0, 1]

for i in range(1, len(adapters)):
    jolt_diff[adapters[i] - adapters[i - 1]] += 1

print(jolt_diff[3] * jolt_diff[1])
