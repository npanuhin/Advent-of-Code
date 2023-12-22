from collections import defaultdict


with open('input.txt') as file:
    workflows = defaultdict(list)
    parts = []

    for line in filter(None, map(str.strip, file)):
        name, properties = line.removesuffix('}').split('{')
        properties = properties.split(',')

        if name:
            for item in properties:
                if ':' in item:
                    condition, next_workflow = item.split(':')
                    workflows[name].append([condition[0], condition[1], int(condition[2:]), next_workflow])
                else:
                    workflows[name].append(item)
        else:
            parts.append({})
            for item in properties:
                key, value = item.split('=')
                parts[-1][key] = int(value)

answer = 0
for part in parts:
    cur_workflow = 'in'

    while cur_workflow not in ('A', 'R'):
        for step in workflows[cur_workflow]:
            if isinstance(step, str):
                cur_workflow = step
                break

            key, condition, value, next_workflow = step

            if condition == '<' and part[key] < value:
                cur_workflow = next_workflow
                break

            if condition == '>' and part[key] > value:
                cur_workflow = next_workflow
                break

    if cur_workflow == 'A':
        answer += sum(part.values())

print(answer)
