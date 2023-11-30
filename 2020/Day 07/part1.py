from re import fullmatch


def count(data, bag, parent_bags):
    parent_bags.add(bag)

    if bag in data:
        for parent_bag in data[bag]:
            count(data, parent_bag, parent_bags)

    return len(parent_bags)


data = {}

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        cur_bag, inner_bags = fullmatch(r"([\w ]+) bags contain ([\w \,]+)\.", line.strip()).groups()

        if inner_bags != "no other bags":

            for bag in inner_bags.split(','):
                n, bag = fullmatch(r" ?(\d+) ([\w ]+) bags?", bag).groups()

                if bag not in data:
                    data[bag] = []

                data[bag].append(cur_bag)

print(count(data, "shiny gold", set()) - 1)
