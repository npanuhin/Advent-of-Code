with open("input.txt", 'r') as file:
    bit_rate = [[0, 0] for _ in range(len(file.readline().strip()))]
    file.seek(0)
    for line in file:
        for i in range(len(bit_rate)):
            bit_rate[i][int(line[i])] += 1

gamma_rate = sum(
    int(item[0] < item[1]) << i
    for i, item in enumerate(reversed(bit_rate))
)

epsilon_rate = (1 << len(bit_rate)) - 1 - gamma_rate

print(gamma_rate * epsilon_rate)
