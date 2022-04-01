horizontal = depth = aim = 0

with open("input.txt", 'r') as file:
    for line in file:
        command, amount = line.split()
        amount = int(amount)

        if command == "forward":
            horizontal += amount
            depth += aim * amount
        elif command == "down":
            aim += amount
        else:
            aim -= amount

print(horizontal * depth)
