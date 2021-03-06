#!/usr/bin/env python3

def get_seat(boarding_pass):
    start, end = 0, 127
    for i in range(0, 7):
        middle = (start + end) // 2
        if boarding_pass[i] == 'F':
            end = middle
        else:
            start = middle+1
    
    row = end

    start, end = 0, 7
    for i in range(7,10):
        middle = (start + end) // 2
        if boarding_pass[i] == 'L':
            end = middle
        else:
            start = middle+1

    return row*8 + start

def main():
    seats = []

    for line in open("./input.txt", "r"):
        new_id = get_seat(line.rstrip())
        seats.append(new_id)

    seats.sort()

    curr = seats[0]
    for i in range(1, len(seats)):
        if seats[i] != curr+1:
            print(curr+1)
            break
        
        curr += 1

if __name__ == '__main__':
    main()