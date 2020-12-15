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
            address_masked = apply_mask(format(int(address), f'0{36}b'), mask)
            
            for address in expand_address(address_masked, 0):
                memory[address] = int(value)

    return memory

def apply_mask(address, mask):
    return ''.join([
        a if m == '0' else m for m, a in zip(mask, address)
    ])

def expand_address(address, index):
    if index == 36:
        yield int(address, 2)
    elif address[index] == 'X':
        yield from expand_address(address[:index] + '0' + address[index+1:], index+1)
        yield from expand_address(address[:index] + '1' + address[index+1:], index+1)
    else:
        yield from expand_address(address, index+1)

def calculate_sum(memory):
    return sum(memory.values())

def main():
    memory = process_input()
    print(calculate_sum(memory))

if __name__ == '__main__':
    main()
