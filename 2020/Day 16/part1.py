with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

line = 0

# Making dictionaty of fields:
fields = {}
while inp[line]:
    fields[inp[line].split(':')[0]] = [list(map(int, range_.split('-'))) for range_ in inp[line].split(':')[1].split("or")]
    line += 1

# Reading my ticket
line += 2
my_ticket = list(map(int, inp[line].split(',')))
line += 3

# Determining valid nearby tickets
sum_of_invalid = 0
while line < len(inp) and inp[line]:
    ticket = list(map(int, inp[line].split(',')))

    for value in ticket:
        if not any(
            any(left <= value <= right for left, right in range_)
            for range_ in fields.values()
        ):
            sum_of_invalid += value

    line += 1

print(sum_of_invalid)
