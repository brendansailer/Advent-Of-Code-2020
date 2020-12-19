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
    # Base: No message left
    if not message:
        return message

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
    count = 0

    message = sys.stdin.readline().strip()
    while message:
        message   = list(message)
        match_42  = 0
        match_31  = 0

        # Consume 42's
        remaining = match_rule(rules, message, curr_state='42')
        while remaining != message:
            message   = remaining
            match_42 += 1
            remaining = match_rule(rules, message, curr_state='42')

        # Consume 31's
        remaining = match_rule(rules, message, curr_state='31')
        while remaining != message:
            message   = remaining
            match_31 += 1
            remaining = match_rule(rules, message, curr_state='31')

        # Must match at least two 42's, one 31, and the difference between 42
        # and 31 matches must be at least one.
        if not message and match_42 >= 2 and match_31 >= 1 and (match_42 - match_31) >= 1:
            count += 1

        message = sys.stdin.readline().strip()

    print(count)

if __name__ == '__main__':
    main()