from re import fullmatch


def count(data, bag, parent_bags=set()):
    parent_bags.add(bag)

    if bag in data:
        for next_bag in data[bag]:
            count(data, next_bag, parent_bags)

    return len(parent_bags)


with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

data = {}

for line in inp:
    cur_bag, inner_bags = fullmatch(r"([\w ]+) bags contain ([\w \,]+)\.", line).groups()

    if inner_bags != 'no other bags':

        for bag in inner_bags.split(','):
            n, bag = fullmatch(r" ?(\d+) ([\w ]+) bags?", bag).groups()

            if bag not in data:
                data[bag] = []

            data[bag].append(cur_bag)

print(count(data, "shiny gold") - 1)
