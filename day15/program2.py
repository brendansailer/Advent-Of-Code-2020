#!/usr/bin/env python3

import collections

def simulate_game(input, stop):
    history = collections.defaultdict(lambda: collections.deque(maxlen=2))

    for index, entry in enumerate(input, 1):
        history[entry].append(index)

    previous = input[-1]
    for turn in range(len(input)+1, stop+1):
        if len(history[previous]) == 1:
            previous = 0
        else:
            previous = history[previous][1] - history[previous][0]

        history[previous].append(turn)


    return previous

def main():
    input = [16,11,15,0,1,7]
    print(simulate_game(input, 30000000))

if __name__ == '__main__':
    main()
