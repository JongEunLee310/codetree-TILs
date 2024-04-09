n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

d = {}.fromkeys(nums, 0)
cnt = 0
for i in range(n):
    if k - nums[i] in d:
        cnt += 1
print(cnt // 2)