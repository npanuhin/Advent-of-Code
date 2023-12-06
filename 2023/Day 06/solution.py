from math import sqrt, floor, ceil


def calc_left_right(time, distance):
    left = floor((time - sqrt(time ** 2 - 4 * distance)) / 2) + 1
    right = ceil((time + sqrt(time ** 2 - 4 * distance)) / 2) - 1
    return left, right


def part1(time, distance):
    answer = 1

    for cur_time, cur_distance in zip(time, distance):
        left, right = calc_left_right(cur_time, cur_distance)
        answer *= (right - left + 1)

    return answer


def part2(time, distance):
    time = int(''.join(map(str, time)))
    distance = int(''.join(map(str, distance)))

    left, right = calc_left_right(time, distance)
    return right - left + 1


with open('input.txt') as file:
    time, distance = (
        list(map(int, line.split(':')[1].split()))
        for line in filter(None, map(str.strip, file))
    )

print(part1(time, distance))
print(part2(time, distance))
