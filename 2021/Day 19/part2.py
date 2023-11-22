from itertools import compress, permutations
from collections import defaultdict
from math import copysign


Vector = tuple[int, int, int]


def vector_rotations(vector: Vector) -> tuple[Vector]:
    variations = set()
    for x, y, z in permutations(vector):
        for flip_x in (-1, 1):
            for flip_y in (-1, 1):
                for flip_z in (-1, 1):
                    variations.add((flip_x * x, flip_y * y, flip_z * z))

    return tuple(variations)


def apply_rotation(scanner: tuple[Vector], rotation: Vector) -> tuple[Vector]:
    result = []
    for reading in scanner:
        result.append([])
        for i in range(len(reading)):
            result[-1].append(reading[abs(rotation[i]) - 1] * int(copysign(1, rotation[i])))
    return result


def add_vectors(vector1: Vector, vector2: Vector) -> Vector:
    return tuple(x + y for x, y in zip(vector1, vector2))


def sub_vectors(vector1: Vector, vector2: Vector) -> Vector:
    return tuple(x - y for x, y in zip(vector1, vector2))


ALL_VECTOR_ROTATIONS = vector_rotations((1, 2, 3))


with open("input.txt", 'r') as file:
    scanner_readings = []

    for line in file:
        if line.startswith("---"):
            scanner_readings.append([])
        elif line.strip():
            scanner_readings[-1].append(tuple(map(int, line.split(','))))

    total_scanners = len(scanner_readings)


scanner_processed = [False] * total_scanners
scanner_processed[0] = True

scanner_positions = [None] * total_scanners
scanner_positions[0] = (0, 0, 0)

while not all(scanner_processed):
    for ref_index in compress(range(total_scanners), scanner_processed):
        ref_scanner = scanner_readings[ref_index]
        for test_index in compress(range(total_scanners), map(lambda processed: not processed, scanner_processed)):
            test_scanner = scanner_readings[test_index]

            for rotation in ALL_VECTOR_ROTATIONS:
                test_rotation = apply_rotation(test_scanner, rotation)

                offsets = defaultdict(int)

                for ref_reading in ref_scanner:
                    for test_reading in test_rotation:
                        offsets[sub_vectors(test_reading, ref_reading)] += 1

                most_common_offset = max(offsets, key=offsets.get)
                if offsets[most_common_offset] >= 12:
                    # print(ref_index, test_index, most_common_offset, offsets[most_common_offset], rotation)
                    scanner_positions[test_index] = add_vectors(most_common_offset, scanner_positions[ref_index])
                    scanner_processed[test_index] = True
                    scanner_readings[test_index] = test_rotation
                    break


# for scanner, shift in zip(scanner_readings, scanner_positions):
#     for i, reading in enumerate(scanner):
#         scanner[i] = sub_vectors(reading, shift)

largest_distance = 0
for i in range(total_scanners):
    for j in range(i + 1, total_scanners):
        largest_distance = max(largest_distance, sum(map(abs, sub_vectors(scanner_positions[i], scanner_positions[j]))))

print(largest_distance)
