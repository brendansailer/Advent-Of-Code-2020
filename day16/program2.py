#!/usr/bin/env python3

import sys
import re
import itertools

def read_rules():
    rules = {}
    line = sys.stdin.readline().strip()

    while line:
        field, ranges = line.split(':')
        rules[field]  = [(int(start), int(end)) for start, end in re.findall(r'(\d+)-(\d+)', ranges)]
        line = sys.stdin.readline().strip()

    return rules

def read_tickets():
    return [[int(field) for field in line.split(',')] for line in sys.stdin if ',' in line]

def is_ticket_valid(rules, ticket):
    return all(any(s <= v <= e for s, e in flatten(rules.values())) for v in ticket)

def flatten(iterable):
    return itertools.chain.from_iterable(iterable)

def find_matches(rules, tickets):
    matches = {}
        
    for field, ranges in rules.items():
        matches[field] = [
            index for index in range(len(tickets[0])) if all(
                any(s <= ticket[index] <= e for s, e in ranges) for ticket in tickets
            )
        ]

    return matches

def find_fields(matches):
    fields = {}

    while matches:
        singles = [(field, indices[0]) for field, indices in matches.items() if len(indices) == 1] # Only one possible mapping

        for field, index in singles:
            fields[index] = field # Record this mapping
            for f in matches:
                matches[f].remove(index) # This index cannot map to other fields, so remove it
            del matches[field] # Ensure we don't find this single again

    return fields

def main():
    rules = read_rules()
    tickets = read_tickets()
    valid_tickets = [ticket for ticket in tickets if is_ticket_valid(rules, ticket)]

    matches = find_matches(rules, valid_tickets) # A dictionary which maps each field to ticket indexes that fit the rules
    fields = find_fields(matches) # Use topological sort to map the fields

    total = 1
    values = [value for index, value in enumerate(tickets[0]) if fields[index].startswith('departure')]
    for value in values:
        total *= value

    print(total)

if __name__ == '__main__':
    main()
