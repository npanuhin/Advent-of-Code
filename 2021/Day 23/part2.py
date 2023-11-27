from heapq import heappush, heappop
from collections import namedtuple


with open("input.txt", 'r') as file:
    house = list(filter(None, (line.strip('\n') for line in file)))
    house = [
        *house[:3],
        '  #D#C#B#A#  ',
        '  #D#B#A#C#  ',
        *house[3:]
    ]
    room_size = len(house) - 3

ENERGY = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

NAMES = (None, 'A', 'B', 'C', 'D')

X_HALLWAY_MAPPING = (1, 2, 4, 6, 8, 10, 11)
X_ROOM_MAPPING = (None, 3, 5, 7, 9)

State = namedtuple("State", ("hall", "room1", "room2", "room3", "room4"))

TARGET_STATE = State(
    # 1    2    4    6    8    10   11
    ('.', '.', '.', '.', '.', '.', '.'),  # Hallway
    ('A',) * room_size, ('B',) * room_size, ('C',) * room_size, ('D',) * room_size  # Rooms
)


def is_hallway_blocked(state, hallway_pos_left, hallway_pos_right):
    return any(
        state.hall[hallway_pos] != '.' for hallway_pos in range(hallway_pos_left, hallway_pos_right + 1)
    )


def move_from_hallway_to_room(state, hallway_pos, room_num):
    if state.hall[hallway_pos] != NAMES[room_num]:  # Does not belong to room
        return None

    if hallway_pos <= room_num:
        if is_hallway_blocked(state, hallway_pos + 1, room_num):  # Hallway is blocked
            return None
    else:
        if is_hallway_blocked(state, room_num + 1, hallway_pos - 1):  # Hallway is blocked
            return None

    # Somebody wrong occupies room slot
    for room_pos in range(room_size):
        if state[room_num][room_pos] != '.' and state[room_num][room_pos] != NAMES[room_num]:
            return None

    for room_pos in range(room_size - 1, -1, -1):  # Search for the lowest slot
        if state[room_num][room_pos] == '.':
            state = list(state)

            state[room_num] = list(state[room_num])
            state[room_num][room_pos] = state[0][hallway_pos]  # Move to room
            state[room_num] = tuple(state[room_num])

            state[0] = list(state[0])
            state[0][hallway_pos] = '.'  # Remove from hallway
            state[0] = tuple(state[0])

            state = State._make(state)
            energy = abs(X_HALLWAY_MAPPING[hallway_pos] - X_ROOM_MAPPING[room_num]) + (room_pos + 1)

            return ENERGY[state[room_num][room_pos]] * energy, state

    return None


def move_from_room_to_hallway(state, room_num, room_pos, hallway_pos):
    # Hallway slot is occupied (covered by is_hallway_blocked, but this check is faster):
    if state.hall[hallway_pos] != '.':
        return None

    for upper_room_pos in range(room_pos):
        if state[room_num][upper_room_pos] != '.':  # Room above us is occupied
            return None

    if hallway_pos <= room_num:
        if is_hallway_blocked(state, hallway_pos, room_num):  # Hallway is blocked
            return None
    else:
        if is_hallway_blocked(state, room_num + 1, hallway_pos):  # Hallway is blocked
            return None

    state = list(state)

    state[0] = list(state[0])
    state[0][hallway_pos] = state[room_num][room_pos]  # Move to hallway
    state[0] = tuple(state[0])

    state[room_num] = list(state[room_num])
    state[room_num][room_pos] = '.'  # Remove from room
    state[room_num] = tuple(state[room_num])

    state = State._make(state)
    energy = abs(X_HALLWAY_MAPPING[hallway_pos] - X_ROOM_MAPPING[room_num]) + (room_pos + 1)

    return ENERGY[state.hall[hallway_pos]] * energy, state


def next_states(state):
    answer = []

    for hallway_pos, item in enumerate(state.hall):  # Move from hallway to room
        if item == '.':
            continue

        for room_num in range(1, 5):
            move = move_from_hallway_to_room(state, hallway_pos, room_num)
            if move is not None:
                answer.append(move)

    for room_num in range(1, 5):  # Move from room to hallway
        for room_pos, item in enumerate(state[room_num]):
            if item == '.':
                continue

            for hallway_pos in range(len(state.hall)):
                move = move_from_room_to_hallway(state, room_num, room_pos, hallway_pos)
                if move is not None:
                    answer.append(move)

    return answer


def print_house(s):
    house = [
        "#############",
        f"#{s.hall[0]}{s.hall[1]}.{s.hall[2]}.{s.hall[3]}.{s.hall[4]}.{s.hall[5]}{s.hall[6]}#",
        f"###{s.room1[0]}#{s.room2[0]}#{s.room3[0]}#{s.room4[0]}###",
    ]

    for i in range(1, room_size):
        house += [f"  #{s.room1[i]}#{s.room2[i]}#{s.room3[i]}#{s.room4[i]}#"]

    house += ["  #########"]
    print('\n'.join(house))


initial_state = State(
    (house[1][1], house[1][2], house[1][4], house[1][6], house[1][8], house[1][10], house[1][11]),
    tuple(house[2 + i][3] for i in range(room_size)),
    tuple(house[2 + i][5] for i in range(room_size)),
    tuple(house[2 + i][7] for i in range(room_size)),
    tuple(house[2 + i][9] for i in range(room_size))
)

seen = {initial_state: 0}
todo = [(0, initial_state)]

while todo:
    score, state = heappop(todo)

    if state == TARGET_STATE:
        print(score)
        break

    for score_diff, next_state in next_states(state):
        if seen.get(next_state, float('inf')) > score + score_diff:
            seen[next_state] = score + score_diff
            heappush(todo, (score + score_diff, next_state))
