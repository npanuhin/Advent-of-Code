def gen_mask(mask, index=0):
    if index == len(mask):
        yield ''.join(mask)

    elif mask[index] != 'X':
        yield from gen_mask(mask, index + 1)

    else:
        mask[index] = '0'
        yield from gen_mask(mask, index + 1)
        mask[index] = '1'
        yield from gen_mask(mask, index + 1)
        mask[index] = 'X'


mem = {}

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line.startswith("mask"):
            mask = line.lstrip("mask").lstrip().lstrip("=").lstrip()

            overwrite_1 = int(mask.replace('X', '0'), 2)
            overwrite_X = int(mask.replace('1', '0').replace('X', '1'), 2)

            mask = list(mask)

        else:
            address, num = map(str.strip, line.split('='))

            address = int(address.lstrip("mem[").rstrip("]"))
            num = int(num)

            address |= overwrite_1
            address &= ~overwrite_X

            for new_mask in gen_mask(mask):

                mem[address | (int(new_mask, 2) & overwrite_X)] = num

print(sum(mem.values()))
