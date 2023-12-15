def hash_algorithm(string: str) -> int:
    value = 0
    for character in string:
        value += ord(character)
        value *= 17
        value %= 256
    return value


with open('input.txt') as file:
    init_seq = list(map(str.strip, file.read().split(',')))

print(sum(
    hash_algorithm(item)
    for item in init_seq
))
