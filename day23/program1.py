#!/usr/bin/env python3

def move_cups(cups):
    for _ in range(100):
        top = cups[0] # Get the current cup and the next 3 clockwise
        next_three = [cups.pop(1) for _ in range(3)]
        max_elem, min_elem = max(cups), min(cups)

        curr = 0 # Find the location to insert the 3 cups
        while top - cups[curr] != 1:
            if curr >= len(cups)-1: # We've reached the end of the list and haven't found the pivot
                if top < min_elem:
                    top = max_elem + 1 # If the element we are searching for is less than the min, wrap around
                else:
                    top -= 1 # try searching for the next smallest element
                curr = 0
            else:
                curr += 1
        
        cups = cups[:curr+1] + next_three + cups[curr+1:] # Insert the 3 cups at the pivot
        
        cups = cups[1:] + cups[:1] # Rotate the cups such that the top cup will be picked next (top cup to the end)

    return cups

def main():
    #cups = [3, 8, 9, 1, 2, 5, 4, 6, 7] # Test cups
    cups = [7, 8, 9, 4, 6, 5, 1, 2, 3] # Input cups
    final_cups = move_cups(cups)
    one_idx = final_cups.index(1)
    print(''.join(str(num) for num in final_cups[one_idx+1:] + final_cups[:one_idx]))
    
if __name__ == '__main__':
    main()