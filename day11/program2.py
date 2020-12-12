#!/usr/bin/env python3

import copy
import collections

DIRECTIONS = [(-1,-1), (1, 1), (-1, 1), (1, -1), (0, -1), (0, 1), (1, 0), (-1, 0)]

def read_input(file_name):
    seats = []
    for line in open(file_name, 'r'):
        seats.append(list(line.strip()))

    return seats

def count_occupied(x, y, seats, x_size, y_size):
    occupied = 0
    for dx, dy in DIRECTIONS:
        x_tmp = x + dx
        y_tmp = y + dy
        while 0 <= y_tmp < y_size and 0 <= x_tmp < x_size: # Move diagonally or left/right/up/down looking for the first open seat
            if seats[y_tmp][x_tmp] == '#':
                occupied += 1
                break
            if seats[y_tmp][x_tmp] == 'L':
                break
            x_tmp += dx
            y_tmp += dy
    
    return occupied

def simulate(seats):
    y_size, x_size = len(seats), len(seats[0])
    new_seats = copy.deepcopy(seats)
    changes = True

    while changes: # If no changes were made, we entered the equlibrium state
        changes = False
        for y in range(y_size):
            for x in range(x_size):
                if seats[y][x] == '.':
                    continue

                occupied = count_occupied(x, y, seats, x_size, y_size)
                if seats[y][x] != '#' and occupied == 0:
                    new_seats[y][x] = '#'
                    changes = True
                elif seats[y][x] == '#' and occupied >= 5:
                    new_seats[y][x] = 'L'
                    changes = True

        seats = copy.deepcopy(new_seats) # Move onto the next iteration since there were changes

    return seats

def count_seats(seats):
    return sum(row.count('#') for row in seats)

def main():
    seats = read_input('input.txt')
    final_seats = simulate(seats)
    print(count_seats(final_seats))

if __name__ == '__main__':
    main()
