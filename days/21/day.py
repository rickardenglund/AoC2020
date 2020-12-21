import re
import puzzle
from datetime import datetime


def main(input):
    print('### day 21 ###')
    start1 = datetime.now()
    p1res = part1(input)
    stop1 = datetime.now()
    print(f'p1: {p1res}')

    start2 = datetime.now()
    p2res = part2(input)
    stop2 = datetime.now()
    print(f'p2: {p2res}')

    print(f'p1 took: {stop1 - start1}\np2 took: {stop2 - start2}')


def part1(input: str) -> int:
    foods = get_input(input)

    possible_allergen = get_possible_allergens(foods)

    ingredients_to_avoid = set()
    for allergen in possible_allergen:
        ingredients_to_avoid = ingredients_to_avoid.union(possible_allergen[allergen])

    count = 0
    for food in foods:
        ingredients, _ = food
        for ingredient in ingredients:
            if ingredient not in ingredients_to_avoid:
                count += 1

    return count


def get_possible_allergens(foods):
    possible_allergen = {}
    all_ingredients = set()
    for food in foods:
        ingredients, allergens = food
        ingredients = set(ingredients)
        for allergen in allergens:
            current_candidates = possible_allergen.get(allergen, ingredients)
            possible_allergen[allergen] = ingredients.intersection(current_candidates)

            all_ingredients = all_ingredients.union(ingredients)
    return possible_allergen


def remove_ingredient(possible_allergens, allergen_name: str):
    for allergen in possible_allergens:
        possible_allergens[allergen] = possible_allergens[allergen].difference([allergen_name])


def part2(input: str) -> str:
    foods = get_input(input)

    possible_allergens = get_possible_allergens(foods)

    solved = []
    while len(solved) < len(possible_allergens):
        for allergen in possible_allergens:
            if len(possible_allergens[allergen]) == 1:
                allergen_name = list(possible_allergens[allergen])[0]
                solved.append((allergen, allergen_name))
                remove_ingredient(possible_allergens, allergen_name)

    solved.sort(key=lambda x: x[0])
    res = []
    for ingredient in solved:
        res.append(ingredient[1])
    return ','.join(res)


def get_input(input: str):
    pattern = re.compile(r'(.*) \(contains (.*)\)')
    matches = pattern.findall(input)

    foods = []
    for food in matches:
        (ingredients, allergens) = food
        foods.append((ingredients.split(' '), allergens.split(', ')))
    return foods


if __name__ == "__main__":
    main(puzzle.input)
