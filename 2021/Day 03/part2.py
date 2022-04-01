def search(array, condition):
    for cur_bit in range(len(array[0])):
        bit_rate = [0, 0]

        for line in array:
            bit_rate[int(line[cur_bit])] += 1

        array = list(filter(lambda line: int(line[cur_bit]) == condition(bit_rate), array))

        if len(array) <= 1:
            break

    return int("".join(map(str, array[0])), 2)


with open("input.txt", 'r') as file:
    report = [list(map(int, line.strip())) for line in file]

print(
    search(report, lambda bit_rate: bit_rate[0] <= bit_rate[1]) *
    search(report, lambda bit_rate: bit_rate[0] > bit_rate[1])
)
