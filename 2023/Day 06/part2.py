from math import sqrt, floor, ceil


with open('input.txt') as file:
    time, distance = (
        int(''.join(line.split(':')[1].split()))
        for line in filter(None, map(str.strip, file))
    )

left = floor((time - sqrt(time ** 2 - 4 * distance)) / 2) + 1
right = ceil((time + sqrt(time ** 2 - 4 * distance)) / 2) - 1

print(right - left + 1)
