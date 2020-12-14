with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

mem = {}

for line in inp:
    if line.startswith("mask"):
        mask = line.lstrip("mask").lstrip().lstrip("=").lstrip()

        mask_xor = int(mask.replace('X', '0'), 2)
        mask_and = int(mask.replace('X', '1'), 2)

    else:
        address, num = map(str.strip, line.split('='))

        address = int(address.lstrip("mem[").rstrip("]"))
        num = int(num)

        mem[address] = (num | mask_xor) & mask_and

print(sum(mem.values()))
