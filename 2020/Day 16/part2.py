def identify_fields(possible_field_pos):
    def gen(b=[]):
        if len(b) == len(possible_field_pos):
            return True

        for item in possible_field_pos[len(b)][1]:
            if item not in (item for i, item in b):
                b.append((possible_field_pos[len(b)][0], item))
                if gen(b) is not None:
                    return b
                b.pop()

    return gen()


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
valid_tickets = []
while line < len(inp) and inp[line]:
    ticket = list(map(int, inp[line].split(',')))

    for value in ticket:
        if not any(
            any(left <= value <= right for left, right in range_)
            for range_ in fields.values()
        ):
            break

    else:
        valid_tickets.append(ticket)

    line += 1

possible_field_pos = [list() for _ in range(len(my_ticket))]

for field_index in range(len(my_ticket)):
    for field, range_ in fields.items():
        if all(
            any(left <= ticket[field_index] <= right for left, right in range_)
            for ticket in valid_tickets
        ):
            possible_field_pos[field_index].append(field)

possible_field_pos = sorted([(i, possible_fields) for i, possible_fields in enumerate(possible_field_pos)], key=lambda x: len(x[1]))

answer = 1
for i, field in identify_fields(possible_field_pos):
    if field.startswith("departure"):
        answer *= my_ticket[i]

print(answer)