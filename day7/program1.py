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
    count = False
    for bag in rules[description]:
        if bag[1] == 'shiny gold':
            return True
        else:
            count = count or get_bags(rules, bag[1])

    return int(count)

def main():
    master_count = 0
    rules = read_input('input.txt')

    for bag in rules.keys():
        master_count += get_bags(rules, bag)

    print(master_count)

if __name__ == '__main__':
    main()