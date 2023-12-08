from math import lcm


with open('input.txt') as file:
    instructions = [item == 'R' for item in next(filter(None, map(str.strip, file)))]
    nodes = {}
    for line in filter(None, map(str.strip, file)):
        key, values = map(str.strip, line.split('='))
        nodes[key] = list(map(str.strip, values.removeprefix('(').removesuffix(')').split(',')))

cur_nodes = [node for node in nodes if node[-1] == 'A']
steps = []
step = 0
while cur_nodes:
    new_nodes = []
    for cur_node in cur_nodes:
        if cur_node[-1] == 'Z':
            steps.append(step)
        else:
            new_nodes.append(
                nodes[cur_node][instructions[step % len(instructions)]]
            )
    cur_nodes = new_nodes
    step += 1

print(lcm(*steps))
