from collections import namedtuple, defaultdict


Cuboid = namedtuple('Cuboid', ['min_x', 'max_x', 'min_y', 'max_y', 'min_z', 'max_z'])

with open("input.txt", 'r') as file:
    reboot_steps = []
    for line in filter(None, file):
        switch, coords = line.split()
        x, y, z = (
            list(map(int, coord[2:].split('..')))
            for coord in coords.split(',')
        )
        reboot_steps.append((
            Cuboid(*x, *y, *z), (1 if switch == 'on' else -1)
        ))


cuboids = defaultdict(int)

for cuboid, mul in reboot_steps:
    new_cuboids = cuboids.copy()

    if mul > 0:
        new_cuboids[cuboid] += mul

    for prev_cuboid in cuboids:
        if prev_cuboid.min_x > cuboid.max_x or cuboid.min_x > prev_cuboid.max_x:
            continue

        if prev_cuboid.min_y > cuboid.max_y or cuboid.min_y > prev_cuboid.max_y:
            continue

        if prev_cuboid.min_z > cuboid.max_z or cuboid.min_z > prev_cuboid.max_z:
            continue

        new_cuboids[Cuboid(
            max(prev_cuboid.min_x, cuboid.min_x),
            min(prev_cuboid.max_x, cuboid.max_x),
            max(prev_cuboid.min_y, cuboid.min_y),
            min(prev_cuboid.max_y, cuboid.max_y),
            max(prev_cuboid.min_z, cuboid.min_z),
            min(prev_cuboid.max_z, cuboid.max_z),
        )] -= cuboids[prev_cuboid]

    cuboids = new_cuboids

volume = 0
for cuboid, mul in cuboids.items():
    volume += (
        (cuboid.max_x - cuboid.min_x + 1) *
        (cuboid.max_y - cuboid.min_y + 1) *
        (cuboid.max_z - cuboid.min_z + 1) *
        mul
    )

print(volume)
