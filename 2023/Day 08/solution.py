from math import lcm


def calc(instructions, cur_nodes, finish_condition):
    steps = []
    step = 0
    while cur_nodes:
        new_nodes = []
        for cur_node in cur_nodes:
            if finish_condition(cur_node):
                steps.append(step)
            else:
                new_nodes.append(
                    nodes[cur_node][instructions[step % len(instructions)]]
                )
        cur_nodes = new_nodes
        step += 1

    return lcm(*steps)


def part1(instructions, nodes):
    return calc(instructions, ['AAA'], lambda node: node == 'ZZZ')


def part2(instructions, nodes):
    return calc(instructions, [node for node in nodes if node[-1] == 'A'], lambda node: node[-1] == 'Z')


with open('input.txt') as file:
    instructions = [item == 'R' for item in next(filter(None, map(str.strip, file)))]
    nodes = {}
    for line in filter(None, map(str.strip, file)):
        key, values = map(str.strip, line.split('='))
        nodes[key] = list(map(str.strip, values.removeprefix('(').removesuffix(')').split(',')))

print(part1(instructions, nodes))
print(part2(instructions, nodes))
