#!/usr/bin/env python3

def read_input(file_name):
    return sorted([int(line.strip()) for line in open(file_name, 'r')])

def configure_adaptors(adaptors):
    one_gap, three_gap = 0, 0

    for i in range(1, len(adaptors)):
        difference = adaptors[i] - adaptors[i-1]
        if difference == 1:
            one_gap += 1
        elif difference == 3:
            three_gap += 1

    return one_gap * three_gap

def main():
    adaptors = read_input('input.txt')
    result = configure_adaptors([0] + adaptors + [adaptors[-1] + 3]) # Start at 0 and end with your device's adaptor
    print(result)

if __name__ == '__main__':
    main()