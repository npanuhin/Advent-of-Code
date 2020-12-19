import re

MAX_DEPTH = 15
STR_REGEX = re.compile(r'\s*"(\w+)"\s*')


def build_regex(rule, depth=0):

    if depth == MAX_DEPTH:
        return ""

    if isinstance(rules[rule], str):
        return rules[rule]

    return "(?:" + "|".join(

        "".join(build_regex(item, depth + 1) for item in subrule)
        for subrule in rules[rule]

    ) + ")"


with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

rules = {}
line = 0
while inp[line]:
    key, value = inp[line].split(':')

    if re.fullmatch(STR_REGEX, value) is None:
        rules[int(key)] = [list(map(int, item.split())) for item in value.split('|')]

    else:
        rules[int(key)] = re.fullmatch(STR_REGEX, value).group(1)

    line += 1

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

regex = re.compile(build_regex(0))

print(sum(
    re.fullmatch(regex, inp[i]) is not None
    for i in range(line + 1, len(inp))
))
