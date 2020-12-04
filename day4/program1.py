#!/usr/bin/env python3

entry = []
count = 0

for line in open("./input.txt", "r"):
    if line == '\n':
        keys = [field.split(':')[0] for field in entry]
        if len(keys) == 8 or (len(keys) == 7 and 'cid' not in keys):
            count += 1
        entry = []
    else:
        data = line.rstrip().split()
        entry.extend(data)

print(count)