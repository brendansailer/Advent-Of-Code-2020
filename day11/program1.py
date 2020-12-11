#!/usr/bin/env python3

import copy

DIRECTIONS = [(-1,-1), (1, 1), (-1, 1), (1, -1), (0, -1), (0, 1), (1, 0), (-1, 0)]

def read_input(file_name):
    seats = []
    for line in open(file_name, 'r'):
        seats.append(list(line.strip()))

    return seats

def apply_rules(seats):
    y_size, x_size = len(seats), len(seats[0])
    new_seats = copy.deepcopy(seats)
    changes = True

    while changes:
        changes = False
        for y in range(y_size):
            for x in range(x_size):
                if seats[y][x] == '.':
                    continue

                occupied = sum([1 for dx, dy in DIRECTIONS if 0 <= y+dy < y_size and 0 <= x+dx < x_size and seats[y+dy][x+dx] == '#'])
                if seats[y][x] != '#' and occupied == 0:
                    new_seats[y][x] = '#'
                    changes = True
                elif seats[y][x] == '#' and occupied >= 4:
                    new_seats[y][x] = 'L'
                    changes = True

        seats = copy.deepcopy(new_seats)

    count = 0
    for y in range(y_size):
        for x in range(x_size):
            if seats[y][x] == '#':
                count += 1
    
    return count

def main():
    seats = read_input('input.txt')
    print(apply_rules(seats))

if __name__ == '__main__':
    main()
