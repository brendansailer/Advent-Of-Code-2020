#!/usr/bin/env python3

import sys

MOVEMENTS = { # Corresponds to the 6 directions from the tile
    'e' : ( 1,  1),
    'se': ( 2, -1),
    'sw': ( 1, -2),
    'w' : (-1, -1),
    'nw': (-2,  1),
    'ne': (-1,  2),
}

def move_tile(instructions):
    x, y = 0, 0

    while instructions:
        if instructions[0] in ('e', 'w'):
            direction, instructions = instructions[0], instructions[1:]
        else: # Direction must be a 2-letter direction
            direction, instructions = instructions[:2], instructions[2:]

        dx, dy = MOVEMENTS[direction]
        x, y = x + dx, y + dy

    return (x, y)

def main():
    locations = {(0,0): 0} # Reference tile starts white

    for line in sys.stdin:
        coords = move_tile(line.strip())
        if coords in locations:
            locations[coords] = (locations[coords] + 1) % 2 # Flip the tiles color using modulo
        else:
            locations[coords] = 1 # All tiles start white, so flip this tile to black since it's the first time we flipped it
    
    print(sum(locations.values())) # Get the count of 1's which are the black tiles
    
if __name__ == '__main__':
    main()