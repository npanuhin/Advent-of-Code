from collections import defaultdict, deque


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

low_pulses = high_pulses = 0

for push in range(1000):
    queue = deque([(output, False, 'broadcaster') for output in modules['broadcaster'][1]])
    low_pulses += 1  # Pressing start button

    while queue:
        module, pulse, recieved_from = queue.popleft()
        if pulse:
            high_pulses += 1
        else:
            low_pulses += 1

        if module not in modules:
            continue
        module_type, outputs = modules[module]

        if module_type == '%':
            if pulse:
                continue
            pulse = module_status[module] = not module_status[module]
        else:
            module_status[module][recieved_from] = pulse
            pulse = not all(module_status[module].values())

        queue.extend((output, pulse, module) for output in outputs)

print(low_pulses * high_pulses)
