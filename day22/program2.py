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
    old_hands = set()

    while player1 and player2:
        if (tuple(player1), tuple(player2)) in old_hands: # Prevent infinite recursion
            return True
        else:
            old_hands.add((tuple(player1), tuple(player2)))

        p1 = player1.pop(0)
        p2 = player2.pop(0)

        if p1 <= len(player1) and p2 <= len(player2):
            winner = simulate_game(player1[:p1], player2[:p2]) # Play a recursed game if they have enough cards (p1 and p2 cards left)
        else:
            winner = True if p1 > p2 else False # Otherwise, the winner is the player with the higher card
    
        if winner: # Handle adding the cards
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)

    return True if player1 else False

def calulate_score(cards):
    return sum(card*multiplier for card, multiplier in zip(cards[::-1], range(1, len(cards)+1))) # Generator expression

def main():
    player1 = read_input()
    player2 = read_input()
    result = player1 if simulate_game(player1, player2) else player2 # player1 and player2 are passed by reference, so we don't need to return them
    print(calulate_score(result))
    
if __name__ == '__main__':
    main()