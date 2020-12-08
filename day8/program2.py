#!/usr/bin/env python3

import re

INSTRUCTION_RE = r'([a-z]{3}) ([+-]\d+)'

def read_input(file_name):
    return [line.strip() for line in open(file_name, 'r')]

def run_instructions(instructions, accumulator, index, visited, augmented):
    if index in visited:
        return
    elif index >= len(instructions):
        print(accumulator)
        return
        
    visited.add(index)
    
    instruction, number = re.findall(INSTRUCTION_RE, instructions[index])[0]
    if instruction == 'acc':
        run_instructions(instructions, accumulator + int(number), index + 1, visited, augmented)
    elif instruction == 'jmp':
        run_instructions(instructions, accumulator, index + int(number), visited, augmented)
        if not augmented:
            run_instructions(instructions, accumulator, index + 1, visited, True)
    else:
        run_instructions(instructions, accumulator, index + 1, visited, augmented)
        if not augmented:
            run_instructions(instructions, accumulator, index + int(number), visited, True)

def main():
    instructions = read_input('input.txt')
    # Start with index and accumulator 0.  Visited set is empty.  We have not made an augmentation (False)
    run_instructions(instructions, 0, 0, set(), False)

if __name__ == '__main__':
    main()