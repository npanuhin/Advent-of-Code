<h1 align="center">🎄 Advent of Code 2020: Day 8 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/8 "Visit adventofcode.com/2020/day/8") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/8/input "Open adventofcode.com/2020/day/8/input").


## Part 1

In Part 1, we were asked to run the code and find an infinite loop in it. The code is a set of lines, each of which contains an instruction and an argument:

- `acc` increases or decreases a single global value called the **accumulator** by the value given in the argument.
- `jmp` **jumps** to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the `jmp` instruction.
- `nop` stands for **No OPeration** - it does nothing. The instruction immediately below it is executed next.

This statement is very useful: *The moment the program tries to run any instruction a second time, you know it will never terminate.*

The following example has a loop:

```
nop +0  ⬊          
acc +1    ⬊         ⬊ 
jmp +4      ↓       ↑  ↓  <- Here the program tries to run the instruction a second time
acc +3      ↓   ⬊  ↑ 
jmp -3      ↓   ↑  ↑ 
acc -99     ↓   ↑    
acc +1       ⬊ ↑   
jmp -4         ↑   
acc +6             
```

Following the statement above, my program executes instructions until it finds an instruction that is executed a second time:

```python
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


with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.split, file.readlines()))

instructions = [[operation, int(argument)] for operation, argument in inp]

print(run_instructions(instructions))
```
```
1614
```
###### Execution time: < 1ms

## Part 2

In Part 2, we were asked to replace one `nop` with `jmp` or one `jmp` with `nop` so that all instructions could be executed to the end (no loops existed).

I haven’t come up with anything smarter than going through all possible changes and finding the one which leads to the correct program execution:

```python
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
```
```
1260
```
###### Execution time: 8 ms
