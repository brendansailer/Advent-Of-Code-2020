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

                occupied = 0
                for dx, dy in DIRECTIONS:
                    x_tmp = x + dx
                    y_tmp = y + dy
                    while 0 <= y_tmp < y_size and 0 <= x_tmp < x_size:
                        if seats[y_tmp][x_tmp] == '#':
                            occupied += 1
                            break
                        if seats[y_tmp][x_tmp] == 'L':
                            break
                        x_tmp += dx
                        y_tmp += dy

                if seats[y][x] != '#' and occupied == 0:
                    new_seats[y][x] = '#'
                    changes = True
                elif seats[y][x] == '#' and occupied >= 5:
                    new_seats[y][x] = 'L'
                    changes = True

        seats = copy.deepcopy(new_seats)

    return seats

def count_seats(seats):
    count = 0
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            if seats[y][x] == '#':
                count += 1
    
    return count

def main():
    seats = read_input('input.txt')
    final_seats = apply_rules(seats)
    print(count_seats(final_seats))

if __name__ == '__main__':
    main()
