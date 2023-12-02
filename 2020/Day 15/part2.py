with open("input.txt") as file:
    inp = list(map(int, file.readline().split(',')))

nums = [None] * 30_000_000
for i, num in enumerate(inp[:-1]):
    nums[num] = i + 1

cur = inp[-1]
for step in range(len(inp), 30_000_000):
    last, nums[cur] = nums[cur], step
    cur = 0 if last is None else step - last

print(cur)
