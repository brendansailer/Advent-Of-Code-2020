#!/usr/bin/env python3

import sys
import collections

def read_food():
    food = collections.defaultdict(list)

    line = sys.stdin.readline().strip()
    while line:
        ingredients, allergens = line.split("(")
        for allergen in allergens[9:-1].split(', '): # Remove the contains and the ')'
            food[allergen].append([ingredient for ingredient in ingredients.split()])
        
        line = sys.stdin.readline().strip()

    return food

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

def confirm_allergens(canidate_allergens): # Topological sorting
    confirmed = dict()

    singled_out = [(allergen, ingredients) for allergen, ingredients in canidate_allergens.items() if len(ingredients) == 1]
    while singled_out:
        for ingredient in singled_out:
            allergen_name, code_name = ingredient[0], ingredient[1][0]
            confirmed[allergen_name] = code_name

            for allergen in canidate_allergens.keys():
                if code_name in canidate_allergens[allergen]:
                    canidate_allergens[allergen].remove(code_name)

        singled_out = [(allergen, ingredients) for allergen, ingredients in canidate_allergens.items() if len(ingredients) == 1]

    return confirmed

def main():
    recepies = read_food()
    canidate_allergens = find_allergens(recepies)
    confirmed_allergens = confirm_allergens(canidate_allergens)
    print(','.join([confirmed_allergens[allergen] for allergen in sorted(confirmed_allergens.keys())]))
    
if __name__ == '__main__':
    main()