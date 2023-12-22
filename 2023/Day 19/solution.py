from collections import defaultdict
from copy import deepcopy
from math import prod


def find_accepted(workflow: str, cur_condition: dict[str, list[int]]):
    for i, step in enumerate(workflows[workflow]):
        if isinstance(step, str):
            if step == 'A':
                yield cur_condition
            elif step != 'R':
                yield from find_accepted(step, cur_condition)
        else:
            key, condition, value, next_workflow = step

            success_condition = deepcopy(cur_condition)
            if condition == '<':
                success_condition[key][1] = min(success_condition[key][1], value - 1)
                cur_condition[key][0] = max(cur_condition[key][0], value)
            elif condition == '>':
                success_condition[key][0] = max(success_condition[key][0], value + 1)
                cur_condition[key][1] = min(cur_condition[key][1], value)

            if next_workflow == 'A':
                yield success_condition
            elif next_workflow != 'R':
                yield from find_accepted(next_workflow, success_condition)


def part1(workflows, parts):
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

    return answer


def part2(workflows):
    return sum(
        prod(right - left + 1 for left, right in condition.values())
        for condition in find_accepted('in', {key: [1, 4000] for key in 'xmas'})
    )


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

print(part1(workflows, parts))
print(part2(workflows))
