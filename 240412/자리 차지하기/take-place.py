from sortedcontainers import SortedSet

n, m = [int(x) for x in input().split()]
chair = [int(x) for x in input().split()]
s = SortedSet([0])
for c in chair:
    upper_bound = s.bisect_right(c)
    if upper_bound <= c and upper_bound <= m:
        s.add(c)
    else:
        break
print(len(s) - 1)