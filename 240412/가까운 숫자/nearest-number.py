from sortedcontainers import SortedSet
from sys import maxsize

n = int(input())
dots = [int(x) for x in input().split()]
s = SortedSet([0])
for i in range(n):
    s.add(dots[i])
    min_dist = maxsize
    for j in range(len(s)):
        upper_bound = s.bisect_right(s[j])
        dist = s[upper_bound] - s[j] if upper_bound < len(s) else maxsize
        min_dist = min(min_dist, dist)
    print(min_dist)