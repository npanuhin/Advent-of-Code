def hash_algorithm(string: str) -> int:
    value = 0
    for character in string:
        value += ord(character)
        value *= 17
        value %= 256
    return value


with open('input.txt') as file:
    init_seq = list(map(str.strip, file.read().split(',')))

boxes = [{} for _ in range(256)]

for item in init_seq:
    if item.endswith('-'):
        label = item.removesuffix('-')

        boxes[hash_algorithm(label)].pop(label, None)

    else:
        label, focal_length = item.split('=')
        focal_length = int(focal_length)

        boxes[hash_algorithm(label)][label] = focal_length

print(sum(
    box_num * slot * focal_length
    for box_num, box in enumerate(boxes, start=1)
    for slot, focal_length in enumerate(box.values(), start=1)
))
