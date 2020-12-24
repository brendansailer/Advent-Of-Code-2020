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

def get_locations():
    locations = {(0,0): 0} # Reference tile starts white

    for line in sys.stdin:
        coords = move_tile(line.strip())
        if coords in locations:
            locations[coords] = (locations[coords] + 1) % 2 # Flip the tiles color using modulo
        else:
            locations[coords] = 1 # All tiles start white, so flip this tile to black since it's the first time we flipped it

    return {loc:color for loc, color in locations.items() if color == 1} # Return black tiles

def count_adjacent(x, y, locations):
    count = 0
    for dx, dy in MOVEMENTS.values():
        if (x+dx, y+dy) in locations:
            count+= 1

    return count

def move_tiles(locations):
    for _ in range(100):
        new_locations = {}

        for x in range(-250, 250):
            for y in range(-250, 250):
                black = count_adjacent(x, y, locations)
                if (x, y) not in locations and black == 2:
                    new_locations[(x,y)] = 1
                elif (x, y) in locations and 1 <= black <= 2:
                    new_locations[(x,y)] = 1

        locations = new_locations

    return locations

def main():
    locations = get_locations()
    new_locations = move_tiles(locations)
    print(len(new_locations))
    
if __name__ == '__main__':
    main()