#!/usr/bin/env python3

SLOPES = [(1,1), (3,1), (5,1), (7,1), (1,2)]

def main():
    graph = []

    for line in open("input.txt"):
        graph.append([char for char in line.rstrip()])

    height = len(graph)
    width = len(graph[0])
    product = 1

    for x_inc, y_inc in SLOPES:
        x, y, count = 0, 0, 0
        while y < height:
            if(graph[y][x] == '#'):
                count += 1
            
            x += x_inc
            y += y_inc

            if x >= width:
                x = x % width
        
        print(count)
        product *= count

    print(product)

if __name__ == '__main__':
    main()