from copy import deepcopy


with open("input.txt", 'r') as file:
    sequence = list(map(int, file.readline().split(',')))

    boards = [[]]
    for line in filter(lambda line: line.strip(), file):
        line = list(map(int, line.split()))

        if len(boards[-1]) == 5:
            boards.append([line])
        else:
            boards[-1].append(line)


has_won = [False] * len(boards)
for number in sequence:
    for board_index, board in enumerate(boards):
        for line in board:
            for i in range(5):
                if line[i] == number:
                    line[i] = None

        for i in range(5):
            if all(board[i][j] is None for j in range(5)) or \
                    all(board[j][i] is None for j in range(5)):

                if not has_won[board_index]:
                    has_won[board_index] = True
                    last_won = deepcopy(board)
                    last_won_number = number


board_sum = sum(
    sum(filter(lambda item: item is not None, line))
    for line in last_won
)

print(board_sum * last_won_number)
