#!/usr/bin/env python3

import sys

def read_input():
    cards = []
    line = sys.stdin.readline().strip()

    while line:
        if line.isdigit():
            cards.append(int(line))
        line = sys.stdin.readline().strip()

    return cards

def simulate_game(player1, player2):
    while player1 and player2:
        p1 = player1.pop(0)
        p2 = player2.pop(0)

        if p1 > p2:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)

    return player1 if player1 else player2

def calulate_score(cards):
    return sum(card*multiplier for card, multiplier in zip(cards[::-1], range(1, len(cards)+1))) # Generator expression

def main():
    player1 = read_input()
    player2 = read_input()
    cards = simulate_game(player1, player2)
    print(calulate_score(cards))
    
if __name__ == '__main__':
    main()