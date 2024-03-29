from collections import deque
from sys import maxsize

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, v, g):
    if not in_range(x, y, len(g[0]), len(g)): return False
    if v[y][x] or g[y][x] == 1: return False

    return True

def push(x, y, v, q, s, dist):
    q.append([y, x])
    v[y][x] = True
    s[y][x] = dist

def bfs(n, g, v, q, s, dxs, dys, dest):
    while q:
        y, x = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, v, g):
                push(nx, ny, v, q, s, s[y][x] + 1)

    min_dist = maxsize
    for y, x in dest:
        if s[y][x] != 0 or s[y][x] == 0 and v[y][x]:
            min_dist = min(min_dist, s[y][x])

    return min_dist if min_dist < maxsize else -1


n, h, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]

# 사람이 서있는 위치를 시작점으로 사용하기 위해 별도의 리스트에 위치 정보 저장, 대피 공간의 위치를 도착점으로 사용하기 위해 위치 정보를 저장
human = []
dest = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2: human.append([i, j])
        if grid[i][j] == 3: dest.append([i, j])

# 사람 수만큼 bfs를 실행하여 사람마다 비를 피할 공간으로 이동하는 최소 거리를 구한다.
dists = []
q = deque()
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
for y, x in human:
    q.append([y, x])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[y][x] = True
    steps = [[0 for _ in range(n)] for _ in range(n)]
    dists.append(bfs(n, grid, visited, q, steps, dx, dy, dest))

h_idx = 0
for i in range(n):
    for j in range(n):
        if h_idx < h and i == human[h_idx][0] and j == human[h_idx][1]:
            print(dists[h_idx], end=' ')
            h_idx += 1
        else: print(0, end=' ')
    print()