nums = sorted([int(x) for x in input().split()])

A = nums[0]
B = nums[1]
C = nums[-1] - A - B

print(A, B, C)