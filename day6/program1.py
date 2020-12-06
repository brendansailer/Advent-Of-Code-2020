#!/usr/bin/env python3

def answer_questions(f):
    answers = set()
    line = f.readline().strip()

    while line:
        [answers.add(char) for char in line]
        line = f.readline().strip()

    return len(answers)

def main():
    master_count = 0
    f = open('input.txt', 'r')
    count = answer_questions(f)

    while count:
        master_count += count
        count = answer_questions(f)

    print(master_count)

if __name__ == '__main__':
    main()