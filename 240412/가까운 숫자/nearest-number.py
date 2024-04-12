from sortedcontainers import SortedSet
from sys import maxsize

n = int(input())
dots = [int(x) for x in input().split()]

s = SortedSet([0])
min_dist = maxsize
for i in range(n):
    s.add(dots[i])
    
    # 입력된 숫자의 위치를 기준으로 왼쪽으로 가장 가까운 숫자와 거리를 구해서 min_dist와 비교
    lower_bound = s.bisect_left(dots[i])
    dist1 = dots[i] - s[lower_bound - 1] if lower_bound < len(s) else maxsize
    min_dist = min(min_dist, dist1)

    # 입력된 숫자의 위치를 기준으로 오른쪽으로 가장 가까운 숫자와 거리를 구해서 min_dist와 비교
    upper_bound = s.bisect_right(dots[i])
    dist2 = s[upper_bound] - dots[i] if upper_bound < len(s) else maxsize
    min_dist = min(min_dist,dist2)

    print(min_dist)