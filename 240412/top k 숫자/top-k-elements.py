from sortedcontainers import SortedSet

n, k = [int(x) for x in input().split()]
s = SortedSet([int(x) for x in input().split()])

for i in range(-1, -k - 1, -1):
    print(s[i], end=' ')