#!/usr/bin/env python3

# TAKEN FROM PBUI

import sys

def read_rules():
    rules = {}

    line = sys.stdin.readline().strip()
    while line:
        number, states = line.split(':', 1)
        states         = [s.strip().replace('"', '').split() for s in states.split(' | ')]
        rules[number]  = states
        line           = sys.stdin.readline().strip()

    return rules

def match_rule(rules, message, curr_state='0'):
    # Base: Match terminal
    if rules[curr_state][0][0].isalpha():
        return message[1:] if rules[curr_state][0][0] == message[0] else message

    # Recursion: Match rule states
    for states in rules[curr_state]:    # Match any
        new_message = message[:]
        all_matched = True
        for next_state in states:       # Match all
            next_message = match_rule(rules, new_message, next_state)
            if next_message == new_message:
                all_matched = False
                break
            new_message = next_message

        if all_matched:
            return new_message

    return message

def main():
    rules = read_rules()
    print(rules)
    count = 0

    message = sys.stdin.readline().strip()
    while message:
        remaining = match_rule(rules, list(message))
        if not remaining:
            count += 1
        message = sys.stdin.readline().strip()

    print(count)

if __name__ == '__main__':
    main()