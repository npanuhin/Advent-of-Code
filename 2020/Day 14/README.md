<h1 align="center">🎄 Advent of Code 2020: Day 14 🎄</h1>
<h6 align="center">by <a href="https://github.com/npanuhin">@npanuhin</a></h6>

> Read the [statement](https://adventofcode.com/2020/day/14 "Visit adventofcode.com/2020/day/14") before watching the solution.
>
> [Get your puzzle input](https://adventofcode.com/2020/day/14/input "Open adventofcode.com/2020/day/14/input").


## Part 1

#### Statement and examples

In Part 1, we were asked to execute an algorithm consisting of the following two types of instructions:

- `mask = {sequence of zeros, ones or letters X}` - sets or updates the bitmask.
- `mem[{address}] = {value}` - applies a bitmask to a `{value} and `writes the result to memory `{address}`.

The bitmask is applied as follows: a `0` or `1` overwrites the corresponding bit in the value, while an `X` leaves the bit in the value unchanged.

For example:

<pre>
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX<b>1</b>XXXX<b>0</b>X
mem[8] = 11
mem[7] = 101
mem[8] = 0
</pre>

Then there are attempts to write the value into memory:

- `mem[8] = 11`:

  The program attempts to write the value `11` to memory address `8`. The value is converted:
  ```
  value:  000000000000000000000000000000001011  (decimal 11)
  mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
  result: 000000000000000000000000000001001001  (decimal 73)
  ```
  Thus, `73` is written to address `8`.

- `mem[7] = 101`: Value `101` is converted using a bitmask to `101` and then is written to address `7`.

- `mem[8] = 0`:  Value `0` is converted using a bitmask to `64` and then is written to address `8`.

At the end, `mem = {8: 64, 7: 101}`

#### Solution

Let's take my solution step by step:

First, I parsed each line and extracted the `bitmask` or `address` with the `value` from it using Python's [`str.lstrip()`](https://docs.python.org/3/library/stdtypes.html#str.lstrip "Visit docs.python.org#str.lstrip") and [`str.rstrip()`](https://docs.python.org/3/library/stdtypes.html#str.rstrip "Visit docs.python.org#str.rstrip") functions.

After that, I used [bitwise operations](https://en.wikipedia.org/wiki/Bitwise_operation "Visit wikipedia.org/Bitwise_operation") to change the value most efficiently:

To force overwrite any bit with `0`, we can use the bitwise `AND` operation (which in python is aliased as `&`) with `0`: `0 and 0 = 0` and `1 and 0 = 0`

To force overwrite any bit with `1`, we can use the bitwise `OR` operation (which in python is aliased as `|`) with `1`: `0 or 1 = 1` and `1 or 1 = 1`

Thus, everything together will look like `value = (value | 11111...) & 00000...`

<!-- Execute code: "part1.py" -->
```python
mem = {}

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line.startswith("mask"):
            mask = line.lstrip("mask").lstrip().lstrip("=").lstrip()

            mask_xor = int(mask.replace('X', '0'), 2)
            mask_and = int(mask.replace('X', '1'), 2)

        else:
            address, value = map(str.strip, line.split('='))

            address = int(address.lstrip("mem[").rstrip("]"))
            value = int(value)

            mem[address] = (value | mask_xor) & mask_and

print(sum(mem.values()))
```
```
12610010960049
```
###### Execution time: 1 ms

## Part 2

In Part 2, we were asked to execute the same algorithm, however now the instructions have changed:

>  Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination **memory address** in the following way:
>  ```
>  If the bitmask bit is 0, the corresponding memory address bit is unchanged.
>  If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
>  If the bitmask bit is X, the corresponding memory address bit is floating.
>  ```

**Floating bit** refers to any possible bit (e.i. `0` or `1`), so if there are several of them in the address, the number of possible addresses becomes `2^k`, where `k` is the number of `X` in the address.

I haven’t come up with anything smarter than iterating over all possible bitmasks: I made a recursive function-generator `gen_mask`. If the entire mask consists only of `X`, then the complexity of this algorithm becomes `O(q * (2 ^ 36))`, which is a lot. However, there are no such tests in the given input.

As I mentioned in Part 1, to replace any bit with `1`, we can use the bitwise `OR` operation (the `overwrite_1` variable).

To deal with `X`, I first create a new mask in which all ones correspond to `X` in the initial mask, and everything else is zero (the `overwrite_X` variable):

```python
mask.replace('1', '0').replace('X', '1')
```

The address is then converted as follows (`~` in Python stands for the boolean `not` operator):

<pre>
Initial mask:           10010<b>X</b>1<b>X</b>01100110101101<b>X</b><b>X</b>10010<b>X</b>110<b>X</b>11
overwrite_1:            100100100110011010110100100100110011
overwrite_X:            00000<b>1</b>0<b>1</b>00000000000000<b>1</b><b>1</b>00000<b>1</b>000<b>1</b>00
~overwrite_X:           11111<b>0</b>1<b>0</b>11111111111111<b>0</b><b>0</b>11111<b>0</b>111<b>0</b>11

------------------------------------------------------------

Initial address:        000000000000000000000011100001100111 (= address)

address:                000000000000000000000011100001100111 (= address)
overwrite_1:            100100100110011010110100100100110011
address | overwrite_1:  100100100110011010110111100101110111

address:                100100100110011010110111100101110111 (= address)
~overwrite_X:           111110101111111111111100111110111011
address & ~overwrite_X: 100100100110011010110100100100110011
</pre>

When a new bitmask is generated (yielded from `gen_mask`) it is also converted using `overwrite_X`. Since the address already has zeros in every place where there are ones of `overwrite_X`, we can merge the new bitmask with the address using the bitwise `OR` operator:

<pre>
Initial mask:           10010<b>X</b>1<b>X</b>01100110101101<b>X</b><b>X</b>10010<b>X</b>110<b>X</b>11
Generated mask:         10010<b>0</b>1<b>0</b>01100110101101<b>0</b><b>0</b>10010<b>1</b>110<b>1</b>11
overwrite_X:            000001010000000000000011000001000100
mask & overwrite_X:     000000000000000000000000000001000100 (= new_mask)

address:                100100100110011010110100100100110011
address | new_mask:     00000000000000000000000000000<b>1</b>000<b>1</b>00
result address:         10010010011001101011010011111<b>1</b>110<b>1</b>11 = 39299272695
</pre>

Finally, the implementation:

<!-- Execute code: "part2.py" -->
```python
def gen_mask(mask, index=0):
    if index == len(mask):
        yield ''.join(mask)

    elif mask[index] != 'X':
        yield from gen_mask(mask, index + 1)

    else:
        mask[index] = '0'
        yield from gen_mask(mask, index + 1)
        mask[index] = '1'
        yield from gen_mask(mask, index + 1)
        mask[index] = 'X'


mem = {}

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line.startswith("mask"):
            mask = line.lstrip("mask").lstrip().lstrip("=").lstrip()

            overwrite_1 = int(mask.replace('X', '0'), 2)
            overwrite_X = int(mask.replace('1', '0').replace('X', '1'), 2)

            mask = list(mask)

        else:
            address, num = map(str.strip, line.split('='))

            address = int(address.lstrip("mem[").rstrip("]"))
            num = int(num)

            address |= overwrite_1
            address &= ~overwrite_X

            for new_mask in gen_mask(mask):

                mem[address | (int(new_mask, 2) & overwrite_X)] = num

print(sum(mem.values()))
```
```
3608464522781
```
###### Execution time: < 1s
