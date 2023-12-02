<h1 align="center">🎄 Advent of Code 2020: Day 3 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/3 "Visit adventofcode.com/2020/day/3") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/3/input "Open adventofcode.com/2020/day/3/input").


## Part 1

In Part 1, we were asked to count the number of trees on a map with specific coordinates, namely:

> From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

However, due to *something about arboreal genetics and biome stability*, the map repeats endlessly to the right. Regarding the code, we can just use the `%` operator on the X-axis: `x % m`

This implementation uses an additional function to get the answer. Although this is not necessary here, it will be very helpful when dealing with Part 2.

<!-- Execute code: "part1.py" -->
```python
def count(field, dx, dy):
    n = len(field)
    m = len(field[0])

    result = 0

    y, x = 0, 0
    while y < n:
        result += field[y][x % m]
        y += dy
        x += dx

    return result


with open("input.txt") as file:
    # Converting input to a two-dimensional bool array
    field = [[place == '#' for place in line.strip()] for line in file]

print(count(field, 3, 1))
```
```
292
```
###### Execution time: < 1ms

## Part 2

In Part 2, we were asked to count the same thing, but for different slopes, and multiply the results.

Since we used the function in Part 1, we can call it for each slope:

<!-- Execute code: "part2.py" -->
```python
def count(field, dx, dy):
    n = len(field)
    m = len(field[0])

    result = 0

    y, x = 0, 0
    while y < n:
        result += field[y][x % m]
        y += dy
        x += dx

    return result


with open("input.txt") as file:
    # Converting input to a two-dimensional bool array
    field = [[place == '#' for place in line.strip()] for line in file]

answer = 1

answer *= count(field, 1, 1)
answer *= count(field, 3, 1)
answer *= count(field, 5, 1)
answer *= count(field, 7, 1)
answer *= count(field, 1, 2)

print(answer)
```
```
9354744432
```
###### Execution time: < 1ms
