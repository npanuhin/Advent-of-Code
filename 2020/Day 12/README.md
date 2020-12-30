<h1 align="center">🎄 Advent of Code 2020: Day 12 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/12 "Visit adventofcode.com/2020/day/12") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/12/input "Open adventofcode.com/2020/day/12/input").


## Part 1

In Part 1, we were asked to navigate the ship using the following actions:

> Action **N** means to move north by the given value.
>
> Action **S** means to move south by the given value.
>
> Action **E** means to move east by the given value.
>
> Action **W** means to move west by the given value.
>
> Action **L** means to turn left the given number of degrees.
>
> Action **R** means to turn right the given number of degrees.
>
> Action **F** means to move forward by the given value in the direction the ship is currently facing.

Suppose the ship is initially at coordinate `(0, 0)`. At the end, its position will be `(END_X, END_Y)`. We should yield the [Manhattan distance](https://en.wikipedia.org/wiki/Manhattan_distance "Visit wikipedia.org/Manhattan_distance") *(sum of the absolute values of its east/west position and its north/south position)* between the starting position and the destination.

To solve this puzzle, I created a dictionary that maps each action to a [**lambda function**](https://docs.python.org/3/reference/expressions.html#lambda "Visit docs.python.org#lambda").

Actions **`N`**, **`S`**, **`E`**, and **`W`** either add or subtract a value from one of the `X` or `Y` coordinates. 

Action **`F`** adds the normalized direction vector multiplied by the given value to the current coordinate, thus moving the ship in the current direction by the distance equal to the given value.

Since the number of degrees in actions **`L`** and **`R`** is often a multiple of `90`, we can store only four directions and switch between them:


```python
DIRECTIONS = ((0, 1), (-1, 0), (0, -1), (1, 0))

'L': direction = (direction - n // 90) % 4
'R': direction = (direction + n // 90) % 4
```

The whole code looks like this:

<!-- Execute code: "part1.py" -->
```python
```
```
```
###### Execution time:

## Part 2

In Part 2, we were asked to count the same [Manhattan distance](https://en.wikipedia.org/wiki/Manhattan_distance "Visit wikipedia.org/Manhattan_distance") between the starting position and the destination. However now almost every action moves not our ship, but rather a **waypoint**:

> Action **N** means to move the **waypoint** north by the given value.
>
> Action **S** means to move the **waypoint** south by the given value.
>
> Action **E** means to move the **waypoint** east by the given value.
>
> Action **W** means to move the **waypoint** west by the given value.
>
> Action **L** means to rotate the **waypoint** around the **ship** counter-clockwise the given number of degrees.
>
> Action **R** means to rotate the **waypoint** around the **ship** clockwise the given number of degrees.
>
> Action **F** means to move forward to the **waypoint** a number of times equal to the given value.

Now each function accepts and returns not only the position of the ship but also the position of the waypoint relative to the ship.

The degrees in actions **L** and **R** are still multiples of `90`:

```python
def rotate(i, j, n):
    for step in range(n % 4):
        i, j = -j, i
    return i, j

'L': i, j = *rotate(i, j, -n // 90),
'R': i, j = *rotate(i, j, n // 90)
```

You may notice that I'm using `n % 4` to find the required number of clockwise rotations. It is possible due to the behavior of Python's modulo operator for negative numbers: `-1 (turn counter-clockwise) % 4 = 3`, which means that one turn `90` degrees counter-clockwise is equal to three turns `90` degrees clockwise.

The whole code looks like this:

<!-- Execute code: "part2.py" -->
```python
```
```
```
###### Execution time:
