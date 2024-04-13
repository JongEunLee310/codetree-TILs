from sortedcontainers import SortedSet

n, m = [int(x) for x in input().split()]
dots = SortedSet([tuple([int(x) for x in input().split()]) for _ in range(n)])
for _ in range(m):
    k = int(input())
    lower_bound = dots.bisect_left((k, 1))
    if lower_bound < len(dots):
        print(dots[lower_bound][0], dots[lower_bound][1])
        dots.remove(dots[lower_bound])
    else:
        print(-1, -1)