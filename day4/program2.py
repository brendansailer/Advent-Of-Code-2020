#!/usr/bin/env python3

import re

def check_height(height):
    try:
        height, units = re.findall(r'^(\d+)(in|cm)$', height)[0]
    except (IndexError, ValueError):
        return False
        
    if units == 'cm':
        return 150 <= int(height) <= 193
    else:
        return 59 <= int(height) <= 76

def main():
    count = 0
    entry = []

    for line in open("./input.txt", "r"):
        if line == '\n':
            passport = {}
            for field in entry:
                key, val = field.split(':')
                passport[key] = val
            
            if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport): # has required fields
                if 1920 <= int(passport['byr']) <= 2002 and 2010 <= int(passport['iyr']) <= 2020 and 2020 <= int(passport['eyr']) <= 2030: # int fields are validated
                    if bool(re.match('^\d{9}$', passport['pid'])) and passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}: # check pid and ecl
                        if bool(re.match(r'^#[0-9a-f]{6}$', passport['hcl'])) and check_height(passport['hgt']):
                            count += 1
            entry = []
        else:
            data = line.rstrip().split()
            entry.extend(data)

    print(count)

if __name__ == '__main__':
    main()