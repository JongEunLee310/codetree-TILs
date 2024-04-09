n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

d = {}
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        try:
            d[nums[i] + nums[j]] += 1
        except:
            d[nums[i] + nums[j]] = 1

print(d[k])