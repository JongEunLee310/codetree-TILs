from sortedcontainers import SortedSet

n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
s = SortedSet([i for i in range(1, m + 1)])
for num in nums:
    s.remove(num)
    print(s[-1])