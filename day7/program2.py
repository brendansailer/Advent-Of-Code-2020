#!/usr/bin/env python3

def read_input(file_name):
    rules = {}
    for line in open(file_name, 'r'):
        outputs = []
        data = line.strip().split('contain')
        for bag in data[1].split(','):
            if bag == ' no other bags.':
                continue
            quantity, detail, color = bag.split('bag')[0].split()
            outputs.append((quantity, detail + ' ' + color))

        rules[data[0].split('bags')[0].strip()] = outputs

    return rules

def get_bags(rules, description):
    count = 0
    for bag in rules[description]:
        count += int(bag[0])
        count += int(bag[0]) * get_bags(rules, bag[1])

    return count

def main():
    rules = read_input('input.txt')
    
    print(get_bags(rules, 'shiny gold'))

if __name__ == '__main__':
    main()