<h1 align="center">🎄 Advent of Code 2020: Day 4 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/4 "Visit adventofcode.com/2020/day/4") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/4/input "Open adventofcode.com/2020/day/4/input").


## Part 1

In Part 1, we were asked to count the number of valid passports. A passport is considered valid if it contains each of the fields `byr`, `iyr`, `eyr`, `hgt`, `hcl`, `ecl`, `pid`. However, it may have other fields, including `cid`, that are not counted.

Here is an example file containing two passports:

```
iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
```

To parse it, we can first split each line by spaces, and then each word by `:`. Thus, we get a `key : value` structure. Finally, we can create a dictionary for each passport to easily validate the fields. I also used Python's [`all()`](https://docs.python.org/3/library/functions.html#all)  function, which is very nice, be sure to check it out (as well as the [`any()`](https://docs.python.org/3/library/functions.html#any)).

<!-- Execute code: "part1.py" -->
```python
fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")  # All fields except "cid"

data = [{}]

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        if not line.strip():
            data.append({})
        else:
            for passport in line.strip().split():
                data[-1][passport.split(':')[0]] = passport.split(':')[1]

print(sum(
    all(field in passport for field in fields)
    for passport in data
))
```
```
250
```
###### Execution time: 2ms

## Part 2

In Part 2, we were asked to count the same fields, except that now each of these fields has strict rules that must be followed in each of them in order for a passport to be valid. I decided to create a dictionary of *lambda* functions for each field and then loop through them to minimize the code. Thanks to [my friend](https://github.com/MarkTheHopeful) for this idea. These *lambda* functions are:

| Name | Description | Function |
|:----:|-------------|----------|
| *byr*  | Four digits; at least 1920 and at most 2002 | <pre lang="python">lambda x: 1920 <= int(x) <= 2002</pre> |
| *iyr*  | Four digits; at least 2010 and at most 2020 | <pre lang="python">lambda x: 2010 <= int(x) <= 2020</pre> |
| *eyr*  | Four digits; at least 2020 and at most 2030 | <pre lang="python">lambda x: 2020 <= int(x) <= 2030</pre> |
| *hgt*  | A number:<br>If followed by `cm`, must be at least 150 and at most 193<br>If followed by `in`, must be at least 59 and at most 76 | <pre lang="python">lambda x:&#010;(x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or&#010;(x[-2:] == "in" and 59 <= int(x[:-2]) <= 76)</pre> |
| *hcl*  | A `#` followed by exactly six characters `0-9` or `a-f`      | <pre lang="python">lambda x: fullmatch(r"#[\da-f]{6}", x)</pre> |
| *ecl*  | Exactly one of:<br>`amb` `blu` `brn` `gry` `grn` `hzl` `oth` | <pre lang="python">lambda x: x in&#010;("amb", "blu", "brn", "gry", "grn", "hzl", "oth")</pre> |
| *pid*  | A nine-digit number, including leading zeroes                | <pre lang="python">lambda x: fullmatch(r"\d{9}", x)</pre> |
| *cid*  | Ignored, missing or not                                      |  |

As you can see, I used `int(x)` in most of the cases. If the string can't be somehow converted to a number, it will raise a `ValueError`, which will be handled in a `try-except` block.

<!-- Execute code: "part2.py" -->
```python
from re import fullmatch


fields = {  # All fields except "cid"
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,

    "hgt": lambda x:
        (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or
        (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76),

    "hcl": lambda x: fullmatch(r"#[\da-f]{6}", x),

    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),

    "pid": lambda x: fullmatch(r"\d{9}", x)
}

data = [{}]

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        if not line.strip():
            data.append({})
        else:
            for passport in line.strip().split():
                data[-1][passport.split(':')[0]] = passport.split(':')[1]

answer = 0

for passport in data:
    if all(field in passport for field in fields):

        for field, checker in fields.items():
            try:
                if not checker(passport[field]):
                    break
            except ValueError:
                break

        else:
            answer += 1

print(answer)
```
```
158
```
###### Execution time: 2ms
