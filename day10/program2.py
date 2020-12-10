#!/usr/bin/env python3

def read_input(file_name):
    return sorted([int(line.strip()) for line in open(file_name, 'r')], reverse=True)

def configure_adaptors(index, adaptors):
    dp = [0]*len(adaptors)
    dp[0] = 1
    
    for i in range(len(adaptors)):
        for j in range(i+1, i+4):
            if j < len(adaptors) and adaptors[i] - adaptors[j] <= 3:
                dp[j] += dp[i]

    return dp[-1]

def main():
    adaptors = read_input('input2.txt')
    count = configure_adaptors(0, [adaptors[0] + 3] + adaptors + [0])
    print(count)

if __name__ == '__main__':
    main()