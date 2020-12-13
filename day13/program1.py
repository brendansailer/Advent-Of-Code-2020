#!/usr/bin/env python3

import sys
import math

def calculate_time():
    time = int(sys.stdin.readline())
    busses = [int(bus) for bus in sys.stdin.readline().split(',') if bus != 'x']

    closest_bus_id = 0
    time_waiting = float('inf')
    for bus in busses:
        departure = math.ceil(time/bus)*bus
        if departure-time < time_waiting:
            time_waiting = departure-time
            closest_bus_id = bus

    return closest_bus_id * time_waiting

def main():
    print(calculate_time())

if __name__ == '__main__':
    main()
