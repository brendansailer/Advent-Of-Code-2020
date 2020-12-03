nums = []

for line in open("input.py"):
    val = line.split()[0]
    nums.append(int(val))

for idx, x in enumerate(nums):
    for num in range(idx, len(nums)):
        y = nums[num]
        for num2 in range(idx+1, len(nums)):
            z = nums[num2]
            if x + y + z == 2020:
                print("The numbers are %d and %d and %d which multiply to: %d", x, y, z, x*y*z)
            