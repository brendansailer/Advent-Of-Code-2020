nums = []

for line in open("./input.txt"):
    occurences, letter, string = line.split()
    start, end = map(int, occurences.split('-'))
    nums.append((start, end, letter[0], string))

count = 0

for start, end, letter, string in nums:
    if start <= string.count(letter) <= end:
        count += 1

count = 0

for start, end, letter, string in nums:
    first = start-1 < len(string) and string[start-1] == letter
    second = end-1 < len(string) and string[end-1] == letter
    if (first or second) and not (first and second):
        count += 1

print(count)