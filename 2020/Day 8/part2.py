def run_instructions(instructions):
    accumulator = 0
    cur_instruction = 0

    visited = [False] * len(instructions)

    while cur_instruction < len(instructions):

        if visited[cur_instruction]:
            return None

        visited[cur_instruction] = True

        operation, argument = instructions[cur_instruction]

        accumulator += argument if operation == "acc" else 0
        cur_instruction += argument if operation == 'jmp' else 1

    return accumulator


with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.split, file.readlines()))

instructions = [[operation, int(argument)] for operation, argument in inp]

for instruction in instructions:

    if instruction[0] == "acc":
        continue

    instruction[0] = "nop" if instruction[0] == "jmp" else "jmp"

    accumulator = run_instructions(instructions)
    if accumulator is not None:
        break

    instruction[0] = "nop" if instruction[0] == "jmp" else "jmp"

print(accumulator)
