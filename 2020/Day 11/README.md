<h1 align="center">🎄 Advent of Code 2020: Day 11 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/11 "Visit adventofcode.com/2020/day/11") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/11/input "Open adventofcode.com/2020/day/11/input").


## Part 1

In Part 1, we were asked *to simulate the process people use to choose (or abandon) their seat in the waiting area* which consists of multiple seats.

> The seat layout fits neatly on a grid. Each position is either floor **`.`**, an empty seat **`L`**, or an occupied seat **`#`**.

The simulation consists of several iterations with the following rules applied to each seat simultaneously in each round:

> If a seat is empty (**`L`**) and there are **no occupied seats adjacent** to it (there are 8 of them), the seat becomes occupied.
>
> If a seat is occupied (**`#`**) and **four or more seats adjacent** to it are also occupied, the seat becomes empty.
>
> Otherwise, the seat's state does not change.

The simulation stops when the layout no longer changes.

In the first part of the puzzle, we can simply model the simulation. I used the `has_occupied` function to answer the question:

*Are there `X` occupied seats adjacent to the seat (`i`, `j`) on the layout `layout1`?*

In the answer we should yield the number of occupied seats in the final layout.

<!-- Execute code: "part1.py" -->

## Part 2

In Part 2 we were asked to simulate the same process, except now the rules that people use to occupy/free a seat have changed:

> People don't just care about **adjacent seats** - they care about **the first seat they can see** in each of those eight directions!
>
> Now, instead of considering just the **eight** immediately adjacent seats, consider the first seat in each of those eight directions.

A solution that calculates these eight adjacent seats for each seat in each iteration will take too long to execute.

Let's notice that the empty spaces do not affect the simulation in any way and the eight seats in each direction for each seat in the layout do not change. Thus, we can pre-calculate the position of these eight seats for each seat in the layout and use them as a `DIRECTIONS` array.

In the implementation below, I used the `sight` array that stores pre-calculated eight positions for each seat:

<!-- Execute code: "part2.py" -->
