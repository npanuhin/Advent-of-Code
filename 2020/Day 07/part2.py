from re import fullmatch


def count(data, bag):
    result = 1

    if bag in data:
        for n, next_bag in data[bag]:
            result += n * count(data, next_bag)

    return result


with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

data = {}

for line in inp:
    cur_bag, inner_bags = fullmatch(r"([\w ]+) bags contain ([\w \,]+)\.", line).groups()

    if inner_bags != 'no other bags':

        if cur_bag not in data:
            data[cur_bag] = []

        for bag in inner_bags.split(','):
            n, bag = fullmatch(r" ?(\d+) ([\w ]+) bags?", bag).groups()

            data[cur_bag].append((int(n), bag))

print(count(data, "shiny gold") - 1)
