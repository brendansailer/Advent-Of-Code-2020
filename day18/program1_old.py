#!/usr/bin/env python3

import sys
import operator

calc = {'+': operator.add, '*': operator.mul}

def find_end(expression, index):
    char = expression[index]
    while char != ')':
        index += 1
        char = expression[index]
    return index

def evaluate(expression, start, end):
    value = None
    index = start
    operator = None

    while index < end:
        char = expression[index]
        print(char)
        if char == '(':
            temp, index = evaluate(expression, index+1, find_end(expression, index))
            if not value:
                value = temp
                end = find_end(expression, index+1)
            else:
                value = calc[operator](value, temp)
        elif char == '+' or char == '*':
            operator = char
        elif char.isnumeric():
            if not value:
                value = int(expression[index])
            else:
                value = calc[operator](value, int(char))

        index += 1

    return value, index

def main():
    total = 0
    for line in sys.stdin:
        print(evaluate(line.strip(), 0, len(line.strip()))[0])
    print(total)

if __name__ == '__main__':
    main()