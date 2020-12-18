#!/usr/bin/env python3

# Taken from pbui

import sys

OPERATORS = ('+', '*')
PARENS    = ('(', ')')

def parse_expression(tokens):
    ''' Parse expression from infix to RPN '''
    # https://en.wikipedia.org/wiki/Shunting-yard_algorithm
    queue = []
    stack = []

    while tokens:
        token = tokens.pop(0)

        if token.isdigit():
            queue.append(int(token))
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] not in PARENS:
                queue.append(stack.pop())
            stack.pop() # Pop the "("
        elif token in OPERATORS:
            while stack and stack[-1] in OPERATORS and stack[-1] >= token: # Pop operators with lower presedence
                queue.append(stack.pop())
            stack.append(token)

    while stack and stack[-1] in OPERATORS:
        queue.append(stack.pop())

    return queue

def evaluate(expression):
    ''' Evaluate RPN expression '''
    stack = []

    while expression:
        token = expression.pop(0)
        if token in OPERATORS:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result   = operand1 + operand2 if token == '+' else operand1 * operand2
        else:
            result   = token
            
        stack.append(result)

    return stack[0]

def main():
    total = 0
    for line in sys.stdin:
        tokens     = [token for token in line if not token.isspace()]
        expression = parse_expression(tokens)
        evaluation = evaluate(expression)
        total     += evaluation

    print(total)

if __name__ == '__main__':
    main()