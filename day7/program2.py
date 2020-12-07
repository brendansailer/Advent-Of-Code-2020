#!/usr/bin/env python3

RULES = {}

def get_bags(description):
    count = 0
    for bag in RULES[description]:
        count += int(bag[0])
        count += int(bag[0]) * get_bags(bag[1])

    return count

def main():
    f = open('input.txt', 'r')
    line = f.readline().strip()

    while line:
        outputs = []
        data = line.split('contain')
        for bag in data[1].split(','):
            if bag == ' no other bags.':
                continue
            quantity, detail, color = bag.split('bag')[0].split()
            outputs.append((quantity, detail + ' ' + color))

        RULES[data[0].split('bags')[0].strip()] = outputs
        line = f.readline().strip()

    print(get_bags('shiny gold'))

if __name__ == '__main__':
    main()