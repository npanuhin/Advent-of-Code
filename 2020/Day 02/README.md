<h1 align="center">🎄 Advent of Code 2020: Day 2 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/2 "Visit adventofcode.com/2020/day/2") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/2/input "Open adventofcode.com/2020/day/2/input").


## Part 1

In Part 1, we were asked to parse the list of passwords and count the number of those that are valid according to the corporate policy.

The input data is in the following format:
```
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```

> Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, `1-3` a means that the password must contain `a` at least 1 time and at most 3 times.
>
> In the above example, 2 passwords are valid.

To parse the input, we can split each line by whitespace. Then we can get boundaries by splitting them by `-` and the target letter by removing `:` at the end. This is a possible implementation:

<!-- Execute code: "part1.py" -->
```python
answer = 0

with open("input.txt", 'r', encoding="utf-8") as file:
	for line in file:
	    boundaries, charecter, string = line.strip().split()

	    lowest, highest = map(int, boundaries.split('-'))
	    charecter = charecter.rstrip(':')

	    if lowest <= string.count(charecter) <= highest:
	        answer += 1

print(answer)
```
```
560
```
###### Execution time: 2 ms

## Part 2

In Part 2, we were asked to parse the same input, but now *exactly one of these positions must contain the given letter*. So we can change only the `if` part. The code below uses the `^` operator, which stands for the [boolean XOR](https://en.wikipedia.org/wiki/Exclusive_or "Visit Wikipedia:Exclusive_or ").

<!-- Execute code: "part2.py" -->
```python
answer = 0

with open("input.txt", 'r', encoding="utf-8") as file:
	for line in file:
	    boundaries, charecter, string = line.strip().split()

	    lowest, highest = map(int, boundaries.split('-'))
	    charecter = charecter.rstrip(':')

	    if (string[lowest - 1] == charecter) ^ (string[highest - 1] == charecter):
	        answer += 1

print(answer)
```
```
303
```
###### Execution time: 2 ms
