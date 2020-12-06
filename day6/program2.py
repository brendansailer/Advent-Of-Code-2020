#!/usr/bin/env python3

import collections

def answer_questions(f):
    data = collections.defaultdict(int)
    people = 0
    line = f.readline().strip()

    while line:
        for char in line:
            data[char] += 1
        line = f.readline().strip()
        people += 1

    # prevent termination early because people != 0 when the file hasn't been read in all the way
    return len([1 for d in data.values() if d == people]), people

def main():
    master_count = 0
    f = open('input.txt', 'r')
    count, people = answer_questions(f)

    while count or people:
        master_count += count
        count, people = answer_questions(f)

    print(master_count)

if __name__ == '__main__':
    main()