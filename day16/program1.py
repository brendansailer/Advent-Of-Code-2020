#!/usr/bin/env python3

import sys
import re

TICKET_RE = r'.*: (\d+-\d+) or (\d+-\d+)'

def read_input():
    fields, nearby_tickets = [], []
    line = sys.stdin.readline().strip()

    while line != '':
        field1, field2 = re.findall(TICKET_RE, line)[0]
        fields.append(field1)
        fields.append(field2)
        line = sys.stdin.readline().strip()

    while line != 'nearby tickets:':
        line = sys.stdin.readline().strip()

    line = sys.stdin.readline().strip()
    while line:
        nearby_tickets.extend(line.split(','))
        line = sys.stdin.readline().strip()

    return fields, nearby_tickets

def check_valid(fields, nearby_tickets):
    valid = set()
    for field in fields:
        for i in range(int(field.split('-')[0]), int(field.split('-')[1])+1):
            valid.add(i)

    invalid = 0
    for ticket in nearby_tickets:
        if int(ticket) not in valid:
            invalid += int(ticket)

    return invalid

def main():
    fields, nearby_tickets = read_input()
    print(check_valid(fields, nearby_tickets))

if __name__ == '__main__':
    main()
