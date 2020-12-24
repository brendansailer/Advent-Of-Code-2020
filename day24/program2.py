#!/usr/bin/env python3

import sys
import itertools

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

def get_locations():
    locations = {(0,0): 0} # Reference tile starts white

    for line in sys.stdin:
        coords = move_tile(line.strip())
        if coords in locations:
            locations[coords] = (locations[coords] + 1) % 2 # Flip the tiles color using modulo
        else:
            locations[coords] = 1 # All tiles start white, so flip this tile to black since it's the first time we flipped it

    return {loc:color for loc, color in locations.items() if color == 1} # Return black tiles

def flatten(iterable):
    return set(itertools.chain.from_iterable(iterable))

def neighbors(x, y):
    return [(x + dx, y + dy) for dx, dy in MOVEMENTS.values()]

def count_black_tiles(x, y, locations):
    return sum(locations.get((x, y), 0) for x, y in neighbors(x, y))

def move_tiles(locations):
    for _ in range(100):
        new_locations = {}
        old_locations = flatten(neighbors(x, y) for x, y in locations.keys())

        for x, y in old_locations:
            black = count_black_tiles(x, y, locations)
            color = locations.get((x, y), 0)
            if color == 0 and black == 2:
                new_locations[(x,y)] = 1
            elif color == 1 and (black == 0 or black > 2):
                new_locations[(x,y)] = 0
            else:
                new_locations[(x,y)] = color

        locations = new_locations

    return locations

def main():
    locations = get_locations()
    new_locations = move_tiles(locations)
    print(sum(new_locations.values()))
    
if __name__ == '__main__':
    main()