<h1 align="center">🎄 Advent of Code 2020: Day 7 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/7 "Visit adventofcode.com/2020/day/7") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/7/input "Open adventofcode.com/2020/day/7/input").


## Part 1

In Part 1, we were asked to parse sentences and count the number of bags that could possibly contain the given `shiny gold` bag.

An example of these sentences:
```
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
```

We can see that each sentence contains a *name* followed by `bags contain` and then either `no other bags` or a comma-separated list of bags. I used [regular expressions](https://en.wikipedia.org/wiki/Regular_expression "Visit wikipedia.org/Regular_expression") for this puzzle. To parse the sentence, I used [this regex](https://regex101.com/r/2O46M8/1) and to strip the name of the bag - [this regex](https://regex101.com/r/vvHX0M/1) (a list of bags can be simply splitted by a comma).

After parsing the sentences, we can run a recursive function to *count the number of bags that can contain the **current bag*** (the initial bag is `shiny gold` of course).

```python
from re import fullmatch


def count(data, bag, parent_bags=set()):
    parent_bags.add(bag)

    if bag in data:
        for parent_bag in data[bag]:
            count(data, parent_bag, parent_bags)

    return len(parent_bags)


with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

data = {}

for line in inp:
    cur_bag, inner_bags = fullmatch(r"([\w ]+) bags contain ([\w \,]+)\.", line).groups()

    if inner_bags != "no other bags":

        for bag in inner_bags.split(','):
            n, bag = fullmatch(r" ?(\d+) ([\w ]+) bags?", bag).groups()

            if bag not in data:
                data[bag] = []

            data[bag].append(cur_bag)

print(count(data, "shiny gold") - 1)
```
```
208
```
###### Execution time: 4 ms

## Part 2

In Part 2, we were asked to count the exact opposite: the number of bags that can fit in a `shiny gold` bag.

To do this, we can swap the keys and values in the `data` dict and start counting again, taking into account the number of bags in each sentence. The regexes above still apply.

```python
from re import fullmatch


def count(data, bag):
    result = 1

    if bag in data:
        for n, child_bag in data[bag]:
            result += n * count(data, child_bag)

    return result


with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

data = {}

for line in inp:
    cur_bag, inner_bags = fullmatch(r"([\w ]+) bags contain ([\w \,]+)\.", line).groups()

    if inner_bags != "no other bags":

        if cur_bag not in data:
            data[cur_bag] = []

        for bag in inner_bags.split(','):
            n, bag = fullmatch(r" ?(\d+) ([\w ]+) bags?", bag).groups()

            data[cur_bag].append((int(n), bag))

print(count(data, "shiny gold") - 1)
```
```
1664
```
###### Execution time: 4 ms
