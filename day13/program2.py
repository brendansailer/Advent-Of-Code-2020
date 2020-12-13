#!/usr/bin/env python3

import sys

# Synchronize the busses one by one, rather than all at once (this allows us to increment the times we try by larger than busses[0] each time)
def get_next_sycn_time(start_time, increment, bus, offset):
    while (start_time + offset) % bus != 0:
        start_time += increment
    
    return start_time

def main():
    _ = sys.stdin.readline()
    busses = sys.stdin.readline().strip().split(',')

    timestamp = int(busses[0])
    increment = timestamp
    offset = 0

    for bus in busses[1:]:
        offset += 1
        if bus == 'x':
            continue

        timestamp = get_next_sycn_time(timestamp, increment, int(bus), offset)
        increment *= int(bus)

    print(timestamp)

if __name__ == '__main__':
    main()
