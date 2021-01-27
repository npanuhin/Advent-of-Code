<h1 align="center">🎄 Advent of Code 2020: Day 15 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/15 "Visit adventofcode.com/2020/day/15") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/15/input "Open adventofcode.com/2020/day/15/input").


## Part 1

In Part 1, we were asked to simulate (at least for now, I haven't found a better solution) the game with the following rules: 

> In this game, the players take turns saying numbers. They begin by taking turns reading from a list of starting numbers (your puzzle input). Then, each turn consists of considering the most recently spoken number:
>
> If that was the first time the number has been spoken, the current player says 0.
> Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was previously spoken.

To store numbers, we can use a [dictionary](https://en.wikipedia.org/wiki/Associative_array), where each number will be matched to its last occurrence: 

```python
nums = {num: last_spoken_index}
```

We can also take advantage of Python's dictionary implementation to get the default value if it is not present using the [`get`](https://docs.python.org/3/library/stdtypes.html#dict.get) function. 

```python
last = nums.get(cur, step)
```

So now `last` contains the index of the last occurrence of the current number. Then we store the index of the current number in the dictionary (`nums[cur] = step`) and calculate the next number (`cur = step - last`).

Thus, if a number has not been spoken, `cur` will be equal to `step (default value) - step = 0`. 

The answer will be the 2020th number spoken:

<!-- Execute code: "part1.py" -->

## Part 2

In Part 2, we were asked to simulate the same game with the same rule, except now until the `30 * 10^6`th step.

As I mentioned earlier, I haven't come up with anything smarter, so this is a 12s+ implementation:

<!-- Execute code: "part2.py" -->