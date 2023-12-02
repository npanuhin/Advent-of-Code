with open("input.txt") as file:
    line = file.readline().strip()

    # Making dictionaty of fields:
    fields = {}
    while line:
        fields[line.split(':')[0]] = [list(map(int, range_.split('-'))) for range_ in line.split(':')[1].split("or")]
        line = file.readline().strip()

    # Reading my ticket
    file.readline()
    my_ticket = list(map(int, file.readline().split(',')))
    file.readline()
    file.readline()
    line = file.readline().strip()

    # Determining valid nearby tickets
    sum_of_invalid = 0
    while line:
        ticket = list(map(int, line.split(',')))

        for value in ticket:
            if not any(
                any(left <= value <= right for left, right in range_)
                for range_ in fields.values()
            ):
                sum_of_invalid += value

        line = file.readline()

print(sum_of_invalid)
