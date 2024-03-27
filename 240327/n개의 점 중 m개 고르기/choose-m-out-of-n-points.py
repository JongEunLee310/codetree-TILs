from sys import maxsize

# 재귀적으로 m개 점을 선택하여 그 그룹의 최대 거리 중 최소 거리를 찾는 함수
def min_dist(dots, m, idx, g):
    if len(g) == m: return max_dist(dots, g, 0, [])
    if idx >= len(dots):
        return max_dist(dots, g, 0, []) if len(g) == m else maxsize

    min_d = maxsize
    # 현재 점을 포함하는 선택
    g.append(idx)
    d1 = min_dist(dots, m, idx + 1, g)

    # 현재 점을 제외하는 선택
    g.pop()
    d2 = min_dist(dots, m, idx + 1, g)

    min_d = min(min_d, d1, d2)

    return min_d

# 재귀적으로 2점을 선택하여 최대 거리를 구하는 함수
def max_dist(dots, g, idx, l):
    if len(l) == 2: return get_dist(dots, g, l)
    if idx >= len(g):
        return get_dist(dots, g, l) if len(l) == 2 else 0 

    max_d = 0
    # 현재 점을 포함하는 거리
    l.append(idx)
    d1 = max_dist(dots, g, idx + 1, l)

    # 현재 점을 제외한 거리
    l.pop()
    d2 = max_dist(dots, g, idx + 1, l)

    max_d = max(max_d, d1, d2)

    return max_d

# 두 점간 유클리디안 거리를 구하는 함수
def get_dist(dots, g, l):
    return (dots[g[l[0]]][0] - dots[g[l[1]]][0]) ** 2 + (dots[g[l[0]]][1] - dots[g[l[1]]][1]) ** 2

n, m = [int(x) for x in input().split()]
dots = [[int(x) for x in input().split()] for _ in range(n)]
print(min_dist(dots, m, 0, []))