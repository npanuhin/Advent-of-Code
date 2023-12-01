from functools import cache


def execute_part(programm, input_value, z=0):
    variables = {'w': input_value, 'x': 0, 'y': 0, 'z': z}

    for command, a, b in programm:
        if isinstance(b, str):
            b = variables[b]

        match command:
            case 'add':
                variables[a] += b
            case 'mul':
                variables[a] *= b
            case 'div':
                variables[a] //= b
            case 'mod':
                variables[a] %= b
            case 'eql':
                variables[a] = variables[a] == b

    return variables


@cache
def search(digit_num, z=0):
    if digit_num == PARTS_AMOUNT:
        return [] if z == 0 else None

    for digit in range(9, 0, -1):
        new_z = execute_part(parts[digit_num], digit, z)['z']

        # The larger this number, the better result you can get, but it will take more time
        # I started with 10 ** 10 and got the answer on 10 ** 8 (takes 13 sec)
        # Later I shrinked it to the following number, which is the minimum amount required for my input (takes 0.5 sec)

        if new_z > 9307514:
            continue

        result = search(digit_num + 1, new_z)
        if result is not None:
            result.append(digit)
            return result


with open('input.txt', 'r') as file:
    programm = list(map(str.split, filter(None, map(str.strip, file))))
    for instruction in programm:
        if instruction[-1] not in ('w', 'x', 'y', 'z'):
            instruction[-1] = int(instruction[-1])

PARTS_AMOUNT = 14

parts = []
for command, *args in programm:
    if command == 'inp':
        parts.append([])
    else:
        parts[-1].append([command, *args])

search_result = search(0)
assert search_result is not None, "Couldn't find solution"

print(''.join(map(str, reversed(search_result))))
