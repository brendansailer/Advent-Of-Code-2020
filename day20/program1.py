#!/usr/bin/env python3

import sys
import collections

def read_tiles():
    tiles = collections.defaultdict(list)
    line = sys.stdin.readline().strip()
    
    while line:
        number = int(line.split(" ")[1][:-1])
        for _ in range(10):
            line = sys.stdin.readline().strip()
            tiles[number].append(line)
        line = sys.stdin.readline().strip() # Read blank line
        line = sys.stdin.readline().strip() # Read tile number

    return tiles

def get_edges(tiles):
    edges = collections.defaultdict(list)

    for number, tile in tiles.items():
        tile_edges = (
            tile[0],
            ''.join([l[0] for l in tile]),
            ''.join([l[9] for l in tile]),
            tile[9],
        )
        
        for edge in tile_edges:
            edges[edge].append(number)
            edges[edge[::-1]].append(number) # When rotating tiles, the edge orentation can flip

    return edges

def find_neighbors(edges):
    results = collections.defaultdict(set)

    for edge, tiles in edges.items():
        for tile1 in tiles:
            for tile2 in tiles:
                if tile1 != tile2: # If two tiles have the same edge and aren't the same tile, they have to be neighbors
                    results[tile1].add(tile2)

    return results

def main():
    tiles = read_tiles()
    edges = get_edges(tiles)
    results = find_neighbors(edges)
    corners = [tile for tile, neighbors in results.items() if len(neighbors) == 2]
    
    total = 1
    for corner in corners:
        total *= corner

    print(total)
    
if __name__ == '__main__':
    main()