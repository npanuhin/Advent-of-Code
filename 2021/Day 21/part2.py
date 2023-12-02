with open("input.txt") as file:
    players = [int(file.readline().split()[-1]) - 1 for _ in range(2)]

MAX_SCORE = 21 + 10
# situations[score1 (MAX_SCORE)][score2 (MAX_SCORE)][cur_pos_player1 (10)][cur_pos_player2 (10)][cur_turn (2)]
situations = [[[
    [[0 for _ in range(2)] for _ in range(10)] for _ in range(10)
] for _ in range(MAX_SCORE)] for _ in range(MAX_SCORE)]

situations[0][0][players[0]][players[1]][0] = 1

wins = [0] * 2

for score_1, layer in enumerate(situations):
    for score_2, layer in enumerate(layer):

        if score_1 >= 21 or score_2 >= 21:  # Game finished
            for player_1_pos, layer in enumerate(layer):
                for player_2_pos, layer in enumerate(layer):
                    wins[0] += layer[1]
                    wins[1] += layer[0]
            continue

        for player_1_pos, layer in enumerate(layer):
            for player_2_pos, (cur_wins_1, cur_wins_2) in enumerate(layer):
                # Player 1
                for roll_1 in range(1, 4):
                    for roll_2 in range(1, 4):
                        for roll_3 in range(1, 4):
                            new_player_1_pos = (player_1_pos + roll_1 + roll_2 + roll_3) % 10
                            new_score1 = score_1 + (new_player_1_pos + 1)
                            situations[new_score1][score_2][new_player_1_pos][player_2_pos][1] += cur_wins_1
                # Player 2
                for roll_1 in range(1, 4):
                    for roll_2 in range(1, 4):
                        for roll_3 in range(1, 4):
                            new_player_2_pos = (player_2_pos + roll_1 + roll_2 + roll_3) % 10
                            new_score2 = score_2 + (new_player_2_pos + 1)
                            situations[score_1][new_score2][player_1_pos][new_player_2_pos][0] += cur_wins_2


print(max(wins))
