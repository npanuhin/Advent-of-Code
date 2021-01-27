with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(int, file.readline().split(',')))

nums = {num: i + 1 for i, num in enumerate(inp[:-1])}

cur = inp[-1]

for step in range(len(inp), 30_000_000):
    last = nums.get(cur, step)
    nums[cur] = step
    cur = step - last

print(cur)
