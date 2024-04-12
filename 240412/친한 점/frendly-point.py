from sortedcontainers import SortedSet

n, m = [int(x) for x in input().split()]
s = SortedSet()
for _ in range(n):
    s.add(tuple([int(x) for x in input().split()]))
for _ in range(m):
    dot = tuple([int(x) for x in input().split()])
    lower_bound = s.bisect_left(dot)
    if lower_bound < len(s):
        print(s[lower_bound][0], s[lower_bound][1])
    else:
        print(-1, -1)