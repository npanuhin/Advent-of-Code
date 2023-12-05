with open('input.txt') as file:
    seeds = list(map(int, file.readline().split(':')[1].split()))

    mappings = {}
    for line in filter(None, map(str.strip, file)):
        if line.endswith(':'):
            source, dest = line.split()[0].split('-to-')
            mappings[source] = [dest, []]
        else:
            mappings[source][1].append(list(map(int, line.split())))

objects = {'seed': seeds}

for source, (dest, mapping) in mappings.items():
    objects[dest] = []
    for obj in objects[source]:
        for dest_start, source_start, range_length in mapping:
            if source_start <= obj < source_start + range_length:
                objects[dest].append(obj + dest_start - source_start)
                break
        else:
            objects[dest].append(obj)


print(min(objects['location']))
