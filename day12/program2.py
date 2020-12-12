#!/usr/bin/env python3

import re

DIRECTION_RE = r'([A-Z])(\d+)'

def read_input(file_name):
    return [line.strip() for line in open(file_name, 'r')]

def move_ferry(action, distance, x, y, wx, wy):
    if action == 'N':
        wy += distance
    elif action == 'S':
        wy -= distance
    elif action == 'E':
        wx += distance
    elif action == 'W':
        wx -= distance
    elif action == 'R':
        for _ in range(distance // 90):
            wx, wy = wy, wx*-1
    elif action == 'L':
        for _ in range(distance // 90):
            wx, wy = wy*-1, wx
    elif action == 'F':
        x += wx*distance
        y += wy*distance

    return x, y, wx, wy

def follow_directions(directions):
    x, y, wx, wy = 0, 0, 10, 1 # Map the NESW directions to an x/y plane

    for entry in directions:
        action, distance = re.findall(DIRECTION_RE, entry)[0]
        x, y, wx, wy = move_ferry(action, int(distance), x, y, wx, wy)

    return abs(x) + abs(y)

def main():
    directions = read_input('input.txt')
    print(follow_directions(directions))

if __name__ == '__main__':
    main()
