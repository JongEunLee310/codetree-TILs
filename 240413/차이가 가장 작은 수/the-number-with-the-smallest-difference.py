from sortedcontainers import SortedSet
from sys import maxsize

n, m = [int(x) for x in input().split()]
s = SortedSet([int(input()) for _ in range(n)])

# 선택된 수보다 m이상이면서 가장 작은 수를 구하기 위해 선택된 수 + m 이상인 수 중 가장 작은 수를 찾는다.
# 탐색한 수와 선택된 수의 차이가 가장 작은 경우를 구한다.
ans = maxsize
for num in s:
    lower_bound = s.bisect_left(num + m)
    ans = min(ans, s[lower_bound] - num if lower_bound < len(s) else maxsize)

print(ans if ans < maxsize else -1)