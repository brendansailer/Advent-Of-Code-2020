#!/usr/bin/env python3

import sys

def read_input():
    return int(sys.stdin.readline().strip())

def find_loopsize(value, target):
    loopsize = 0

    while value != target:
        loopsize += 1
        value *= 7
        value %= 20201227

    return loopsize

def calculate_public_key(subject_number, loopsize):
    value = 1
    for _ in range(loopsize):
        value *= subject_number
        value %= 20201227

    return value

def main():
    door = read_input()
    card = read_input()
    door_loopsize = find_loopsize(1, door)
    card_loopsize = find_loopsize(1, card)
    print(calculate_public_key(card, door_loopsize))
    print(calculate_public_key(door, card_loopsize))

if __name__ == '__main__':
    main()