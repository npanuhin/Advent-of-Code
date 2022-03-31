<h1 align="center">🎄 Advent of Code 2020: Day 6 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/6 "Visit adventofcode.com/2020/day/6") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/6/input "Open adventofcode.com/2020/day/6/input").


## Part 1

In Part 1, we were asked to count the number of letters (questions) contained in at least one of given lines (people). This is easy to implement using a [set](https://en.wikipedia.org/wiki/Set_(abstract_data_type)): let's call the [`union`](https://docs.python.org/3/library/stdtypes.html#frozenset.union) method for each line or its alias - bitwise `|` (`|=`) operator.

The sum of these counts for each group of people will be the answer.

<!-- Execute code: "part1.py" -->
```python
data = [set()]

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        if not line.strip():
            data.append(set())
        else:
            data[-1] |= set(line.strip())

print(sum(len(group) for group in data))
```
```
6506
```
###### Execution time: 2ms

## Part 2

In Part 2, we were asked to count the same thing, except that now **every** line must contain the given letter. Thus, we can change the [`union`](https://docs.python.org/3/library/stdtypes.html#frozenset.union) method to [`intersection`](https://docs.python.org/3/library/stdtypes.html#frozenset.intersection) (`&` operator):

<!-- Execute code: "part2.py" -->
```python
from string import ascii_letters


data = [set(ascii_letters)]

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        if not line.strip():
            data.append(set(ascii_letters))
        else:
            data[-1] &= set(line.strip())

print(sum(len(group) for group in data))
```
```
3243
```
###### Execution time: 3ms
