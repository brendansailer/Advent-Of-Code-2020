nums = []

for line in open("input.py"):
    val = line.split()[0]
    nums.append(int(val))

for idx, x in enumerate(nums):
    for num in range(idx, len(nums)):
        y = nums[num]
        if x != y and x + y == 2020:
            print("The numbers are %d and %d which multiply to: %d", x, y, x*y)
            