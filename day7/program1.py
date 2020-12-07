#!/usr/bin/env python3

RULES = {}

def get_bags(description):
    count = False
    for bag in RULES[description]:
        if bag[1] == 'shiny gold':
            return True
        else:
            count = count or get_bags(bag[1])

    return int(count)

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

    master_count = 0
    for bag in RULES.keys():
        master_count += get_bags(bag)

    print(master_count)

if __name__ == '__main__':
    main()