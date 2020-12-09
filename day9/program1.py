#!/usr/bin/env python3

def read_input(file_name):
    return [int(line.strip()) for line in open(file_name, 'r')]

def two_sum(seen, target):
    history = set()
    for num in seen:
        complement = target - num
        if complement in history:
            return True
        else:
            history.add(num)
    
    return False

def check_sequence(preamble_length, data):
    seen = set()
    for i in range(preamble_length):
        seen.add(data[i])
    
    for index in range(preamble_length, len(data)):
        target = data[index]

        if not two_sum(seen, target):
            return target
        
        seen.remove(data[index-preamble_length])
        seen.add(target)

    return -1

def main():
    data = read_input('input.txt')
    number = check_sequence(25, data)
    print(number)

if __name__ == '__main__':
    main()