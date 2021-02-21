<h1 align="center">🎄 Advent of Code 2020: Day 10 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/10 "Visit adventofcode.com/2020/day/10") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/10/input "Open adventofcode.com/2020/day/10/input").


## Part 1

In Part 1, we were asked to **count the differences** in the *jolt* adapter array. Adapter array stands for the following:

Each adapter has a specific *output voltage* and is capable of accepting an input voltage `1`, `2` or `3` jolts lower than the output.

Also:
- Your device has a built-in joltage adapter rated for `3` jolts higher than the highest-rated adapter in the array.
- The initial charging outlet has an effective joltage rating of `0`.

First, let's sort the array and count the difference between each consistent pair of adapters. It is easy to prove that if we connect the adapters in a sorted order, we can use the maximum possible number of adapters.

The answer should be the number of 1-jolt differences multiplied by the number of 3-jolt differences.

My implementation below uses the `jolt_diff` array, which indicates the number of `0`, `1`, `2`, or `3` jolt differences:

<!-- Execute code: "part1.py" -->
```python
with open("input.txt", 'r', encoding="utf-8") as file:
    adapters = sorted(list(map(int, file)) + [0])

jolt_diff = [0, 0, 0, 1]

for i in range(1, len(adapters)):
    jolt_diff[adapters[i] - adapters[i - 1]] += 1

print(jolt_diff[3] * jolt_diff[1])
```
```
2368
```
###### Execution time: < 1ms

## Part 2

In Part 2, we were asked to *count the total number of distinct ways one can arrange the adapters to connect the charging outlet to the device*.

This puzzle can be solved using [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming "Visit wikipedia.org/Dynamic_programming"):
let's count *the number of ways one can arrange the adapters to connect the charging outlet to the **current adapter***.

Consider the current adapter with the `X` jolt output. The puzzle statement says that it can take from `X - 3` to `X - 1` jolts. Thus, *the number of ways...* is equal to the sum of *the number of ways* for adapters with values `X - 3` to `X - 1`.

The last thing one must remember is storing an array for dynamic programming. I came to the conclusion that it's best to make a dictionary rather then a list, since in general the joltage value can be very large. In the implementation below, I used Python's [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict "Visit docs.python.org#collections.defaultdict") instead of a regular `dict`, because it allows to take a `value` for any `key` (returning the default value, in this case: `0`).

<!-- Execute code: "part2.py" -->
```python
from collections import defaultdict


with open("input.txt", 'r', encoding="utf-8") as file:
    adapters = sorted(list(map(int, file)) + [0])

adapters.append(adapters[-1] + 3)

ways = defaultdict(lambda: 0, {0: 1})

for adapter in adapters:
    for parent_adapter in range(adapter - 3, adapter):
        ways[adapter] += ways[parent_adapter]

print(ways[adapters[-1]])
```
```
1727094849536
```
###### Execution time: < 1ms
