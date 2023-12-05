def check_range(start, end):
    if start < end:
        yield start, end


def split_range(start, end, split_start, split_end):
    yield from check_range(start, min(end, split_start))  # left
    yield from check_range(max(start, split_start), min(end, split_end))  # center
    yield from check_range(max(start, split_end), end)  # right


with open('input.txt') as file:
    seeds = list(map(int, file.readline().split(':')[1].split()))
    seeds = [
        [seeds[i], seeds[i] + seeds[i + 1]]
        for i in range(0, len(seeds), 2)
    ]

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

    # Step 1: split all ranges by mapping boundaries
    splittted = objects[source]
    for dest_start, source_start, range_length in mapping:
        splittted = [
            new_range
            for start, end in splittted
            for new_range in split_range(start, end, source_start, source_start + range_length)
        ]

    # Step 2: apply mapping to each range
    for start, end in splittted:
        for dest_start, source_start, range_length in mapping:
            if source_start <= start and end <= source_start + range_length:
                objects[dest].append([
                    start + dest_start - source_start,
                    end + dest_start - source_start
                ])
                break
        else:
            objects[dest].append((start, end))

print(min(start for start, end in objects['location']))
