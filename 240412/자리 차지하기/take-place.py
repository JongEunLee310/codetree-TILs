from sortedcontainers import SortedSet

n, m = [int(x) for x in input().split()]
chair = [int(x) for x in input().split()]
s = SortedSet([0])
for c in chair:
    lower_bound = s.bisect_left(c)
    if lower_bound <= c and lower_bound <= m:
        s.add(c)
    else:
        break
print(len(s) - 1)