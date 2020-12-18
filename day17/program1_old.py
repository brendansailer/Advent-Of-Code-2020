#!/usr/bin/env python3

import sys
import pprint
import copy

DIRECTIONS = [(-1,-1,-1), (1, 1,-1), (-1, 1,-1), (1, -1,-1), (0, -1,-1), (0, 1,-1), (1, 0,-1), (-1, 0,-1),
              (-1,-1, 0), (1, 1, 0), (-1, 1, 0), (1, -1, 0), (0, -1, 0), (0, 1, 0), (1, 0, 0), (-1, 0, 0),
              (-1,-1, 1), (1, 1, 1), (-1, 1, 1), (1, -1, 1), (0, -1, 1), (0, 1, 1), (1, 0, 1), (-1, 0, 1),
            ]

def read_input():
    return [[list(line.strip()) for line in sys.stdin]]

def expand_grid(grid):
    blank = ['.']*(len(grid[0])+2)
    end_cap = [blank.copy() for _ in range((len(grid[0])+2))]

    expanded_grid = [end_cap]
    for z_grid in grid:
        expanded_grid.append([blank.copy()] + [['.'] + line + ['.'] for line in z_grid] + [blank.copy()]) # Use a copy, not a reference
    return expanded_grid + [end_cap]

def simulate(grid):
    expanded_grid = expand_grid(grid)
    pprint.pprint(expanded_grid)
    new_grid = copy.deepcopy(expanded_grid)
    z_size, y_size, x_size = len(expanded_grid), len(expanded_grid[0]), len(expanded_grid[0][0])

    for z in range(z_size):
        for y in range(y_size):
            for x in range(x_size):
                active = sum([1 for dx, dy, dz in DIRECTIONS if 0 <= z+dz < z_size and 0 <= y+dy < y_size and 0 <= x+dx < x_size and expanded_grid[z+dz][y+dy][x+dx] == '#'])
                if expanded_grid[z][y][x] == '#' and (active != 2 and active != 3):
                    new_grid[z][y][x] = '.'
                elif expanded_grid[z][y][x] == '.' and active == 3:
                    new_grid[z][y][x] = '#'

    return new_grid

def count_active(grid):
    return sum(row.count('#') for row in grid)

def main():
    grid = read_input()

    #for _ in range(3):
    grid = simulate(grid)
    pprint.pprint(grid)
    #pprint.pprint([''.join(line) for line in grid])

if __name__ == '__main__':
    main()
