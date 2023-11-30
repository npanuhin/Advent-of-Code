with open("input.txt", 'r', encoding="utf-8") as file:
    food = [
        (
            set(ingredients.split()),
            set(map(str.strip, allergens.strip().removeprefix("contains").split(',')))
        )
        for ingredients, allergens in (line.strip().removesuffix(')').split('(') for line in file)
    ]

mapped_ingredients = {}
mapped_allergens = {}

for ingredients, allergens in food:

    for allergen in allergens:
        if allergen not in mapped_allergens:
            mapped_allergens[allergen] = ingredients.copy()
        else:
            mapped_allergens[allergen] &= ingredients

while mapped_allergens:
    allergen = min(mapped_allergens, key=lambda key: len(mapped_allergens[key]))

    ingredient = next(iter(mapped_allergens.pop(allergen)))

    mapped_ingredients[ingredient] = allergen

    for key in mapped_allergens:
        mapped_allergens[key].discard(ingredient)


print(','.join(sorted(mapped_ingredients, key=lambda ingredient: mapped_ingredients[ingredient])))
