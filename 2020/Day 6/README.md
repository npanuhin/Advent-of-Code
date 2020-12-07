<h1 align="center">🎄 Advent of Code 2020: Day 6 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/6 "Visit adventofcode.com/2020/day/6") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/6/input "Open adventofcode.com/2020/day/6/input").


## Part 1

In Part 1, we were asked to count the number of letters (questions) contained in at least one of given lines (people). This is easy to implement using a [set](https://en.wikipedia.org/wiki/Set_(abstract_data_type)): let's call the `union` method for each line.

The sum of these counts for each group of people will be the answer.

```python
with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

data = [set()]

for line in inp:
    if not line:
        data.append(set())
    else:
        data[-1] = data[-1].union(line)

print(sum(len(group) for group in data))
```
```
6506
```

## Part 2

In Part 2, we were asked to count the same thing, except that now **every** line must contain the given letter. Thus, we can change the `union` method to `intersection`:

```python
from string import ascii_letters

with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

data = [set(ascii_letters)]

for line in inp:
    if not line:
        data.append(set(ascii_letters))
    else:
        data[-1] = data[-1].intersection(line)

print(sum(len(group) for group in data))
```
```
3243
```
