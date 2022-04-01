with open("input.txt", 'r') as file:
    sequence = list(map(int, file.readline().split(',')))

    boards = [[]]
    for line in filter(lambda line: line.strip(), file):
        line = list(map(int, line.split()))

        if len(boards[-1]) == 5:
            boards.append([line])
        else:
            boards[-1].append(line)

winner_board = None
for number in sequence:
    for board in boards:
        for line in board:
            for i in range(5):
                if line[i] == number:
                    line[i] = None

        for i in range(5):
            if all(board[i][j] is None for j in range(5)) or \
                    all(board[j][i] is None for j in range(5)):
                winner_board = board

    if winner_board:
        break

board_sum = sum(
    sum(filter(lambda item: item is not None, line))
    for line in winner_board
)

print(board_sum * number)
