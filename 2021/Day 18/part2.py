from copy import deepcopy

SnailfishNumber = list[int]


def set_leftmost_of_right(number: SnailfishNumber, value: int):
    if number is None:
        return

    if isinstance(number[1], int):
        number[1] += value
        return
    number = number[1]

    while not isinstance(number[0], int):
        number = number[0]
    number[0] += value


def set_rightmost_of_left(number: SnailfishNumber, value: int):
    if number is None:
        return

    if isinstance(number[0], int):
        number[0] += value
        return
    number = number[0]

    while not isinstance(number[1], int):
        number = number[1]
    number[1] += value


def fix_nested(
    number: SnailfishNumber,
    cur_level: int = 0,
    nearest_left_parent: SnailfishNumber = None,
    nearest_right_parent: SnailfishNumber = None
):
    if isinstance(number, int):
        return

    if cur_level == 4:
        return number

    # Going to the left
    cur_result = fix_nested(number[0], cur_level + 1, nearest_left_parent, number)
    if cur_result is not None:
        left, right = cur_result
        number[0] = 0
        if left is not None:
            set_rightmost_of_left(nearest_left_parent, left)
        if right is not None:
            set_leftmost_of_right(number, right)

    # Going to the right
    cur_result = fix_nested(number[1], cur_level + 1, number, nearest_right_parent)
    if cur_result is not None:
        left, right = cur_result
        number[1] = 0
        if left is not None:
            set_rightmost_of_left(number, left)
        if right is not None:
            set_leftmost_of_right(nearest_right_parent, right)


def fix_greater(number: SnailfishNumber) -> bool:
    for i, item in enumerate(number):
        if isinstance(item, int):
            if item >= 10:
                a = item >> 1  # floor(item / 2)
                b = item & 1  # item % 2
                number[i] = [a, a + b]
                return True
        elif fix_greater(item):
            return True
    return False


def snail_reduce(input_number: SnailfishNumber):
    while True:
        fix_nested(input_number)
        if not fix_greater(input_number):
            return


def add(a: SnailfishNumber, b: SnailfishNumber) -> SnailfishNumber:
    answer = [a, b]
    snail_reduce(answer)
    return answer


def save_add(a: SnailfishNumber, b: SnailfishNumber) -> SnailfishNumber:
    answer = [deepcopy(a), deepcopy(b)]
    snail_reduce(answer)
    return answer


def magnitude(number: SnailfishNumber) -> int:
    if isinstance(number, int):
        return number
    return 3 * magnitude(number[0]) + 2 * magnitude(number[1])


with open("input.txt", 'r') as file:
    numbers = list(map(eval, filter(None, map(str.strip, file))))

print(max(
    magnitude(save_add(a, b))
    for a in numbers
    for b in numbers
    if a != b
))
