#!/usr/bin/env python3

def simulate_game(input, stop):
    history = {}
    for index, entry in enumerate(input, 1):
        history[entry] = [index]

    previous = input[-1]
    for turn in range(len(input)+1, stop+1):
        if len(history[previous]) == 1:
            previous = 0 # Speak 0
            history[previous].append(turn)
        else:
            previous = turn - 1 - history[previous][-2] # Speak the diff between when it was spoken last and now
            if previous in history:
                history[previous].append(turn)
            else:
                history[previous] = [turn]

    return previous

def main():
    input = [16,11,15,0,1,7]
    print(simulate_game(input, 2020))

if __name__ == '__main__':
    main()
