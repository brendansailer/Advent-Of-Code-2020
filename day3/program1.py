#!/usr/bin/env python3

def main():
    graph = []
    x, y = 0, 0

    for line in open("input.txt"):
        graph.append([char for char in line.rstrip()])

    count = 0
    while y < len(graph):
        if(graph[y][x] == '#'):
            count += 1
        
        x += 3
        y += 1

        if x >= len(graph[0]):
            x = x % len(graph[0])

    print(count)

if __name__ == '__main__':
    main()