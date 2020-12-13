from math import ceil

with open("input.txt", 'r', encoding="utf-8") as file:
    departure_time = int(file.readline())
    buses = set(map(
        lambda x: None if x == 'x' else int(x),
        file.readline().split(',')
    ))

buses.discard(None)

first_bus, wait = None, float('inf')

for bus in buses:
    bus_time = ceil(departure_time / bus) * bus

    if bus_time - departure_time < wait:
        wait = bus_time - departure_time
        first_bus = bus

print(first_bus * wait)
