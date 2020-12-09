#!/usr/bin/env python3

def read_input(file_name):
    return [int(line.strip()) for line in open(file_name, 'r')]

def slide_window(target, data):
    start, end, total = 0, 0, data[0]

    while end < len(data):
        if total == target:
            return min(data[start:end+1]) + max(data[start:end+1])
        elif total < target:
            end += 1
            total += data[end]
        else:
            total -= data[start]
            start += 1

def main():
    data = read_input('input.txt')
    number = slide_window(21806024, data)
    print(number)

if __name__ == '__main__':
    main()