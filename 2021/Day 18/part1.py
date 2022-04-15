from functools import reduce


EMPTY_RESULT = [None, None, False]
RESULT = [None, None, True]


def check_nested(cur, n=4):
    for i, item in enumerate(cur):
        if isinstance(item, int):
            continue

        if n == 1:
            result = [*item, True]
            cur[i] = 0
        elif not (result := check_nested(item, n - 1))[2]:
            continue

        if result[(j := not i)] is not None:
            if isinstance(cur[j], int):
                cur[j] += result[j]
            else:
                cur = cur[j]
                while not isinstance(cur[i], int):
                    cur = cur[i]
                cur[i] += result[j]

            result[j] = None
        return result

    return EMPTY_RESULT


def check_greater(cur):
    for i, item in enumerate(cur):
        if isinstance(item, int):
            if item >= 10:
                a = item >> 1
                b = item & 1
                cur[i] = [a, a + b]
                return True
        elif check_greater(item):
            return True

    return False


def snail_reduce(input_number):
    while check_nested(input_number)[2] or check_greater(input_number):
        pass

    return input_number


def add(number1, number2):
    return snail_reduce([number1, number2])


def magnitude(number):
    if isinstance(number, int):
        return number
    return 3 * magnitude(number[0]) + 2 * magnitude(number[1])


with open("input.txt", 'r') as file:
    numbers = tuple(map(eval, filter(lambda line: line, map(str.strip, file))))

print(magnitude(reduce(add, numbers)))
