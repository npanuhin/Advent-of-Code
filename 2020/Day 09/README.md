<h1 align="center">🎄 Advent of Code 2020: Day 9 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/9 "Visit adventofcode.com/2020/day/9") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/9/input "Open adventofcode.com/2020/day/9/input").


## Part 1

In Part 1, we were asked to find an invalid instance in a set of numbers that obeys the following rule:

> First, `25` numbers are initialized. After that, each number must be the sum of any two of the `25` immediately previous numbers (these two numbers must be different).

I find the task quite easy because it has such a small input range of `25`. The simplest solution will have complexity `O(25^2 * n) = O(n)`

<!-- Execute code: "part1.py" -->
```python
def find_first_invalid(numbers):
    for k in range(25, len(numbers)):
        if not any(
            numbers[i] + numbers[j] == numbers[k]
            for i in range(k - 25, k)
            for j in range(i + 1, k)
        ):
            return numbers[k]


with open("input.txt") as file:
    inp = list(map(int, file))

print(find_first_invalid(inp))
```
```
133015568
```
###### Execution time: 6ms

## Part 2

In Part 2, we were asked to ***find a contiguous set of at least two numbers which sum to the invalid number***.

We can leave the `find_first_invalid` function unchanged. However, after finding the first invalid number, we must find the range (from `range_start` to `range_end`), that adds up to this invalid number. Let's use the [two pointer technique](https://www.geeksforgeeks.org/two-pointers-technique):

We will iterate over `range_start` and adjust `range_end` each time. Since each pointer (`range_start` and `range_end`) runs at most `n`, the complexity this method provides will be `O(n)`.

Having `range_start` and `range_end` for each iteration, as well as the sum that can be calculated by adding or removing one element at each step (again, `O(n)`), we can check if the sum is equal to the invalid number and if so, that's the answer.

In the answer we should yield the sum of the smallest and largest number in this range:

<!-- Execute code: "part2.py" -->
```python
def find_first_invalid(numbers):
    for k in range(25, len(numbers)):
        if not any(
            numbers[i] + numbers[j] == numbers[k]
            for i in range(k - 25, k)
            for j in range(i + 1, k)
        ):
            return numbers[k]


with open("input.txt") as file:
    inp = list(map(int, file))

invalid_num = find_first_invalid(inp)

summ = 0
range_end = -1
for range_start in range(len(inp)):
    while summ < invalid_num:
        range_end += 1
        summ += inp[range_end]

    if summ == invalid_num and range_start != range_end:
        print(
            min(inp[i] for i in range(range_start, range_end + 1)) +
            max(inp[i] for i in range(range_start, range_end + 1))
        )

    summ -= inp[range_start]
```
```
16107959
```
###### Execution time: 6ms
