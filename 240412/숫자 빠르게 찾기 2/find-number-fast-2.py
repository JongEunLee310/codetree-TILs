from sortedcontainers import SortedSet

n, m = [int(x) for x in input().split()]
s = SortedSet([int(x) for x in input().split()])
for _ in range(m):
    num = int(input())
    lower_bound = s.bisect_left(num)
    print(s[lower_bound] if lower_bound != None and lower_bound < len(s) else -1)