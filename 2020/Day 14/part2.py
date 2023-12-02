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

with open("input.txt") as file:
    for line in map(str.strip, file):

        if line.startswith("mask"):
            mask = line.removeprefix("mask = ")

            overwrite_1 = int(mask.replace('X', '0'), 2)
            overwrite_x = int(mask.replace('1', '0').replace('X', '1'), 2)

            mask = list(mask)

        else:
            address, num = map(str.strip, line.split('='))

            address = int(address.removeprefix("mem[").removesuffix("]"))
            num = int(num)

            address |= overwrite_1
            address &= ~overwrite_x

            for new_mask in gen_mask(mask):

                mem[address | (int(new_mask, 2) & overwrite_x)] = num

print(sum(mem.values()))
