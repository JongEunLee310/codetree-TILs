from sortedcontainers import SortedSet

n, m = [int(x) for x in input().split()]
chair = [int(x) - 1 for x in input().split()]
s = SortedSet()
for c in chair:
    lower_bound = s.bisect_left(c)
    if lower_bound <= c:
        s.add(c)
    else:
        break
print(len(s))