n = int(input())
nums = sorted([int(x) for x in input().split()])

diff = []
for i in range(n):
    diff.append(nums[i + n] - nums[i])
print(min(diff))