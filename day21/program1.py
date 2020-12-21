#!/usr/bin/env python3

import sys
import collections

def read_food():
    all_ingredients = collections.defaultdict(int)
    food = collections.defaultdict(list)

    line = sys.stdin.readline().strip()
    while line:
        ingredients, allergens = line.split("(")

        for allergen in allergens[9:-1].split(', '): # Remove the contains and the ')'
            food[allergen].append([ingredient for ingredient in ingredients.split()])

        for ingredient in ingredients.split():
            all_ingredients[ingredient] += 1 
        
        line = sys.stdin.readline().strip()

    return food, all_ingredients

def find_allergens(recepies):
    allergens = {}

    for allergen, all_recepies in recepies.items():
        counter = collections.defaultdict(int)
        for recepie in all_recepies: # List of all recipe involving the allergen
            for ingredient in recepie: # All ingredients in that recipe
                counter[ingredient] += 1
        
        total_items = len(all_recepies)
        allergens[allergen] = [ingredient for ingredient, count in counter.items() if count == total_items] # Find common items

    return allergens

def get_non_allergens(ingredients, allergens): # Non-allergens never appear in canidate allergens for any food
    return [ingredient for ingredient in ingredients if all(ingredient not in canidates for allergen, canidates in allergens.items())]

def main():
    recepies, all_ingredients = read_food()
    canidate_allergens = find_allergens(recepies)
    non_allergens = get_non_allergens(all_ingredients, canidate_allergens)
    print(sum(all_ingredients[non_allergen] for non_allergen in non_allergens))
    
if __name__ == '__main__':
    main()