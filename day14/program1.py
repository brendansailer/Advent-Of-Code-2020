#!/usr/bin/env python3

import sys
import re

MASK_RE = r'mask = ([01X]+)'
MEM_RE = r'mem\[(\d+)\] = (\d+)'

def process_input():
    memory = {}
    mask = None

    for line in sys.stdin:
        if line.startswith("mask"):
            mask = re.findall(MASK_RE, line.strip())[0]
        else:
            address, value = re.findall(MEM_RE, line.strip())[0]
            memory[address] = apply_mask(format(int(value), f'0{36}b'), mask)

    return memory

def apply_mask(value, mask):
    result = [v if m == 'X' else m for m, v in zip(mask, value)]
    return int(''.join(result), 2)

def calculate_sum(memory):
    return sum(memory.values())

def main():
    memory = process_input()
    print(calculate_sum(memory))

if __name__ == '__main__':
    main()
