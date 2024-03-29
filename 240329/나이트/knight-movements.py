from collections import deque

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, v, n):
    if not in_range(x, y, n, n): return False
    if v[y][x]: return False

    return True

# 이전 노드의 거리 + 1을 현재 노드에 저장
def push(x, y, v, q, s, dist):
    q.append([y, x])
    v[y][x] = True
    s[y][x] = dist

# 최단거리를 구하기 위해 검사 중인 노드에 거리 정보를 갱신하며 이동
def bfs(n, v, q, s, dxs, dys, ex, ey):
    while q:
        y, x = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, v, n):
                push(nx, ny, v, q, s, s[y][x] + 1)

    return s[ey][ex] if s[ey][ex] != 0 or s[ey][ex] == 0 and visited[ey][ex] else -1

n = int(input())
r1, c1, r2, c2 = [int(x) - 1 for x in input().split()]
visited = [[False for _ in range(n)] for _ in range(n)]
visited[r1][c1] = True
q = deque()
q.append([r1, c1])
steps = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [1, 2, 2, 1, -1, -2, -2, -1], [-2, -1, 1, 2, 2, 1, -1, -2]
print(bfs(n, visited, q, steps, dx, dy, c2, r2))