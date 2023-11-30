mem = {}

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in map(str.strip, file):

        if line.startswith("mask"):
            mask = line.removeprefix("mask = ")

            mask_xor = int(mask.replace('X', '0'), 2)
            mask_and = int(mask.replace('X', '1'), 2)

        else:
            address, value = map(str.strip, line.split('='))

            address = int(address.removeprefix("mem[").removesuffix("]"))
            value = int(value)

            mem[address] = (value | mask_xor) & mask_and

print(sum(mem.values()))
