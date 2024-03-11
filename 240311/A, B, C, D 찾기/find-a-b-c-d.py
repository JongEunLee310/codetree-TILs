nums = sorted([int(x) for x in input().split()])

A, B = nums[0], nums[1]
C, D = 0, 0
for i in range(2, len(nums)):
    if nums[i] <= A + B:
        C = nums[i]
        D = nums[-1] - A - B - C
        if not D in nums:
            C, D = 0, 0
        else:
            break

print(A, B, C, D)