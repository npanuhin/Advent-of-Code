mem = {}

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line.startswith("mask"):
            mask = line.lstrip("mask").lstrip().lstrip("=").lstrip()

            mask_xor = int(mask.replace('X', '0'), 2)
            mask_and = int(mask.replace('X', '1'), 2)

        else:
            address, value = map(str.strip, line.split('='))

            address = int(address.lstrip("mem[").rstrip("]"))
            value = int(value)

            mem[address] = (value | mask_xor) & mask_and

print(sum(mem.values()))
