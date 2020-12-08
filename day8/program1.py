#!/usr/bin/env python3

import re

INSTRUCTION_RE = r'([a-z]{3}) ([+-]\d+)'

def read_input(file_name):
    return [line.strip() for line in open(file_name, 'r')]

def run_instructions(instructions):
    accumulator, index = 0, 0
    visited = set()

    while index not in visited:
        visited.add(index)

        instruction, number = re.findall(INSTRUCTION_RE, instructions[index])[0]
        if instruction == 'acc':
            accumulator += int(number)
            index += 1
        elif instruction == 'jmp':
            index += int(number)
        else:
            index += 1

    return accumulator

def main():
    instructions = read_input('input.txt')
    accumulator = run_instructions(instructions)
    print(accumulator)

if __name__ == '__main__':
    main()