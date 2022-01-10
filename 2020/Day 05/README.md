<h1 align="center">🎄 Advent of Code 2020: Day 5 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/5 "Visit adventofcode.com/2020/day/5") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/5/input "Open adventofcode.com/2020/day/5/input").


## Part 1

In Part 1, we were asked to count the ID for every seat on a plane with ***binary** space partitioning*. For example:

Consider the seat `FBFBBFFRLR`:

- The first 7 letters `FBFBBFF` specify one of the 128 rows - from `0` to `127`:

    **F** stands for the front half and **B** stands for the back.

    Thus, in this example the algorithm would be: `0-127 > (F) > 0-63 > (B) > 32-63 > (F) > 32-47...`

- The last 3 letters `RLR` specify one of the 8 columns - from `0` to `7`:

    **R** stands for the right half and **L** stands for the left.

    Thus, in this example the algorithm would be: `0-7 > (R) > 4-7 > (L) > 4-5 > (R) > 5`

> Read the [statement](https://adventofcode.com/2020/day/5 "Visit adventofcode.com/2020/day/5") for a complete example

The result is the maximum ID of those counted. Nothing interesting here, I just implemented two binary searches:

<!-- Execute code: "part1.py" -->
```python
max_ID = -1

with open("input.txt", 'r', encoding="utf-8") as file:
    for string in file:
        string = string.strip()

        left, right = 0, 128
        for i in range(7):
            middle = (left + right) // 2

            if string[i] == 'B':
                left = middle
            else:
                right = middle

        row = left

        left, right = 0, 8
        for i in range(7, 10):
            middle = (left + right) // 2

            if string[i] == 'R':
                left = middle
            else:
                right = middle

        column = left

        ID = row * 8 + column

        max_ID = max(max_ID, ID)

print(max_ID)
```
```
855
```
###### Execution time: 1 ms

## Part 2

In Part 2, we were asked to count the same IDs (so the main code was left untouched).

However, this time the answer is the only ID that is not present in the list. It can be found because the entire list contains IDs from `i-th` seat to `j-th`, except one seat with `ID = k` (`i < k < j`) is skipped.

To find this ID, I sorted all IDs and ran through them in a loop, looking for the first ID that is not equal to the first + its number. For example, in the following list...

```
756
757
758
760
761
762
```

...that is `760`, because `760 != 756 + 3`. The answer will be this ID minus 1, which is `759`.

<!-- Execute code: "part2.py" -->
```python
IDs = []

with open("input.txt", 'r', encoding="utf-8") as file:
    for string in file:
        string = string.strip()

        left, right = 0, 128
        for i in range(7):
            middle = (left + right) // 2

            if string[i] == 'B':
                left = middle
            else:
                right = middle

        row = left

        left, right = 0, 8
        for i in range(7, 10):
            middle = (left + right) // 2

            if string[i] == 'R':
                left = middle
            else:
                right = middle

        column = left

        IDs.append(row * 8 + column)

IDs.sort()

for i in range(len(IDs)):
    if IDs[i] != IDs[0] + i:
        print(IDs[i] - 1)
        break
```
```
552
```
###### Execution time: 1 ms
