with open("input.txt", 'r', encoding="utf-8") as file:
    departure_time = int(file.readline())
    buses = list(map(
        lambda x: None if x == 'x' else int(x),
        file.readline().split(',')
    ))

jump = buses[0]
timestamp = 0

for delta, bus in enumerate(buses):
    if delta != 0 and bus is not None:

        while (timestamp + delta) % bus != 0:
            timestamp += jump
        jump *= bus

print(timestamp)
