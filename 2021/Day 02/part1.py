horizontal = depth = 0

with open("input.txt", 'r') as file:
    for line in file:
        command, amount = line.split()
        amount = int(amount)

        if command == "forward":
            horizontal += amount
        elif command == "down":
            depth += amount
        else:
            depth -= amount

print(horizontal * depth)
