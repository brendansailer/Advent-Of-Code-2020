#!/usr/bin/env python3

import re

DIRECTION_RE = r'([A-Z])(\d+)'
HEADING = {0:'E', 90:'S', 180:'W', 270:'N'}

def read_input(file_name):
    return [line.strip() for line in open(file_name, 'r')]

def move_ferry(action, distance, x, y, heading):
    if action == 'N':
        y += distance
    elif action == 'S':
        y -= distance
    elif action == 'E':
        x += distance
    elif action == 'W':
        x -= distance
    elif action == 'R':
        heading += distance
    elif action == 'L':
        heading -= distance
    elif action == 'F':
        return move_ferry(HEADING[heading % 360], distance, x, y, heading)

    return x, y, heading

def follow_directions(directions):
    x, y, heading = 0, 0, 0 # Map the NESW directions to an x/y plane and the ship starts heading East (defined as 0 for the problem)

    for entry in directions:
        action, distance = re.findall(DIRECTION_RE, entry)[0]
        x, y, heading = move_ferry(action, int(distance), x, y, heading)

    return abs(x) + abs(y)

def main():
    directions = read_input('input.txt')
    print(follow_directions(directions))

if __name__ == '__main__':
    main()
