from math import sqrt, floor, ceil


with open('input.txt') as file:
    time, distance = (
        list(map(int, line.split(':')[1].split()))
        for line in filter(None, map(str.strip, file))
    )

answer = 1

for cur_time, cur_distance in zip(time, distance):
    left = floor((cur_time - sqrt(cur_time ** 2 - 4 * cur_distance)) / 2) + 1
    right = ceil((cur_time + sqrt(cur_time ** 2 - 4 * cur_distance)) / 2) - 1
    answer *= (right - left + 1)

print(answer)
