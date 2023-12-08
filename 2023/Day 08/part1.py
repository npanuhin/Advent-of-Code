with open('input.txt') as file:
    instructions = [item == 'R' for item in next(filter(None, map(str.strip, file)))]
    nodes = {}
    for line in filter(None, map(str.strip, file)):
        key, values = map(str.strip, line.split('='))
        nodes[key] = list(map(str.strip, values.removeprefix('(').removesuffix(')').split(',')))

cur_node = 'AAA'
step = 0
while cur_node != 'ZZZ':
    cur_node = nodes[cur_node][instructions[step % len(instructions)]]
    step += 1

print(step)
