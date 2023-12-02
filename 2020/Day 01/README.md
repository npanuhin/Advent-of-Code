<h1 align="center">🎄 Advent of Code 2020: Day 1 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/1 "Visit adventofcode.com/2020/day/1") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/1/input "Open adventofcode.com/2020/day/1/input").


## Part 1

In Part 1, we were asked to **find two entries that add up to 2020** in a given list of numbers, and then multiply them to get the result. This can be done by brute-forcing with the complexity `O(n^2)`:

```python
with open("input.txt") as file:
    inp = list(map(int, file.readlines()))

for i in range(len(inp) - 1):
    for j in range(i + 1, len(inp)):
        if inp[i] + inp[j] == 2020:
            print(inp[i] * inp[j])
```
```
928896
```

However, using binary search, we can reduce the complexity to `O(n log(n))`:

<!-- Execute code: "part1.py" -->
```python
with open("input.txt") as file:
    inp = sorted(map(int, file))

for i in range(len(inp) - 1):

    left, right = i + 1, len(inp)
    while right - left > 1:
        middle = (left + right) // 2

        if inp[middle] <= 2020 - inp[i]:
            left = middle
        else:
            right = middle

    if inp[i] + inp[left] == 2020 and left != i:
        print(inp[i] * inp[left])
```
```
928896
```
###### Execution time: < 1ms

## Part 2

In Part 2, we were asked to do the same thing, but with **three numbers**: find **tree** entries that add up to 2020 in a given list of numbers, and then multiply them to get the result. Again, brute-force algorithm is easy to implement, but using binary search, we can reduce the complexity from `O(n^3)` to `O(n^2 log(n))`.

In the implementation below, I've added additional `breaks` to reduce the execution time from `34ms` to less than `1ms`, although the complexity is still `O(n^2 log(n))`.

<!-- Execute code: "part2.py" -->
```python
with open("input.txt") as file:
    inp = sorted(map(int, file))

for i in range(len(inp) - 2):
    if inp[i] * 3 >= 2020:
        break

    for j in range(i + 1, len(inp) - 1):

        if inp[i] + inp[j] * 2 >= 2020:
            break

        left, right = j + 1, len(inp)
        while right - left > 1:
            middle = (left + right) // 2

            if inp[middle] <= 2020 - inp[i] - inp[j]:
                left = middle
            else:
                right = middle

        if inp[i] + inp[j] + inp[left] == 2020 and left != i and left != j:
            print(inp[i] * inp[j] * inp[left])
```
```
295668576
```
###### Execution time: < 1ms
