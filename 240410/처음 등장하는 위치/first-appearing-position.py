from sortedcontainers import SortedDict

n = int(input())
nums = [int(x) for x in input().split()]

s = SortedDict()
for i in range(1, n + 1):
    if nums[i - 1] not in s:
        s[nums[i - 1]] = i

for key, item in s.items():
    print(key, item)