with open("input.txt", 'r', encoding="utf-8") as file:
    departure_time = int(file.readline())
    buses = [None if i == 'x' else int(i) for i in file.readline().split(',')]

jump = buses[0]
timestamp = 0

for delta, bus in enumerate(buses):
    if delta != 0 and bus is not None:

        while (timestamp + delta) % bus != 0:
            timestamp += jump
        jump *= bus

print(timestamp)
