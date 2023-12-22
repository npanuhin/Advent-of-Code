from collections import defaultdict, deque
from math import lcm


with open('input.txt') as file:
    modules = {}
    for line in filter(None, map(str.strip, file)):
        module, output = map(str.strip, line.split('->'))
        outputs = list(map(str.strip, output.split(',')))
        if module == 'broadcaster':
            module_type = None
        else:
            module_type, module = module[0], module[1:]
        modules[module] = (module_type, outputs)

inputs = defaultdict(list)
for module, (_, outputs) in modules.items():
    for output in outputs:
        inputs[output].append(module)

module_status = {
    module: (False if module_type == '%' else {input_module: False for input_module in inputs[module]})
    for module, (module_type, _) in modules.items()
}

final_module = next(module for module, (_, outputs) in modules.items() if 'rx' in outputs)
assert all(modules[module][0] == '&' for module in inputs[final_module])

count = {module: None for module in inputs[final_module]}

push = 0
while not all(count.values()):
    queue = deque([(output, False, 'broadcaster') for output in modules['broadcaster'][1]])
    push += 1

    while queue:
        module, pulse, recieved_from = queue.popleft()

        if module not in modules:
            continue
        module_type, outputs = modules[module]

        if module_type == '%':
            if pulse:
                continue
            pulse = module_status[module] = not module_status[module]
        else:
            if module in count and not count[module] and not pulse:
                count[module] = push

            module_status[module][recieved_from] = pulse
            pulse = not all(module_status[module].values())

        queue.extend((output, pulse, module) for output in outputs)

print(lcm(*count.values()))
