def run_instructions(instructions):
    accumulator = 0
    cur_instruction = 0

    visited = [False] * len(instructions)

    while cur_instruction < len(instructions):

        if visited[cur_instruction]:
            return accumulator

        visited[cur_instruction] = True

        operation, argument = instructions[cur_instruction]

        accumulator += argument if operation == "acc" else 0
        cur_instruction += argument if operation == 'jmp' else 1


with open("input.txt") as file:
    instructions = [[operation, int(argument)] for operation, argument in (line.split() for line in file)]

print(run_instructions(instructions))
