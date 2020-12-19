#!/usr/bin/env python3

import sys

def get_rules():
    rules = {}
    canidates = []
    for line in sys.stdin:
        if ':' in line:
            rule_number, requirements = line.strip().split(':')

            requirements = requirements.strip().split('|')
            if len(requirements) == 2: # x y | a b
                value = [requirement.strip().replace(" ", "") for requirement in requirements]
            elif requirements[0][0] == "\"": # "a"
                value = requirements[0][1]
            else:
                value = requirements[0].replace(" ", "")

            rules[rule_number] = value
        elif line != '\n':
            canidates.append(line.strip())

    return rules, canidates

def create_outcomes(outcomes, rules, curr_rule):
    if isinstance(curr_rule, list):
        duo = []
        for rule in curr_rule:
            temp = create_outcomes(outcomes, rules, rule)
            duo.append(temp)

        return duo

    elif curr_rule.isalpha():
        return curr_rule 

    else:
        temp = ['']
        for char in curr_rule:
            result = create_outcomes(outcomes, rules, rules[char])
            if isinstance(result, list):
                if isinstance(result[0], str):
                    a = [s + result[0] for s in temp]
                    b = [s + result[1] for s in temp]
                    temp = a + b
                else:
                    a, b = [], []
                    for r in result[0]:
                        a += [s + r for s in temp]
                    for r in result[1]:
                        b += [s + r for s in temp]
                    temp = a + b
            else:
                temp = [s + result for s in temp]

        if curr_rule == rules['0']:
            for t in temp:
                outcomes.add(t)
        if len(temp) == 1:
            return temp[0]
        else:
            return temp

def main():
    rules, canidates = get_rules()
    print(rules, canidates)
    outcomes = set()
    create_outcomes(outcomes, rules, rules['0'])
    print(outcomes)

    total = 0
    for c in canidates:
        if c in outcomes:
            total += 1
            print(c)

    print(total)

if __name__ == '__main__':
    main()