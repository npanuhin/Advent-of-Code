from re import fullmatch


def count(data, bag):
    result = 1

    if bag in data:
        for n, child_bag in data[bag]:
            result += n * count(data, child_bag)

    return result


data = {}

with open("input.txt", 'r', encoding="utf-8") as file:
    for line in file:
        cur_bag, inner_bags = fullmatch(r"([\w ]+) bags contain ([\w \,]+)\.", line.strip()).groups()

        if inner_bags != "no other bags":

            if cur_bag not in data:
                data[cur_bag] = []

            for bag in inner_bags.split(','):
                n, bag = fullmatch(r" ?(\d+) ([\w ]+) bags?", bag).groups()

                data[cur_bag].append((int(n), bag))

print(count(data, "shiny gold") - 1)
