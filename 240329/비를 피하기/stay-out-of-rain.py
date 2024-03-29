from collections import deque
from sys import maxsize

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, o, v, g):
    if not in_range(x, y, len(g[0]), len(g)): return False
    if o in v[y][x] or g[y][x] == 1: return False

    return True

def push(x, y, o, v, q, s, dist):
    q.append([y, x, o])
    v[y][x][o] = True
    s[y][x][o] = [dist, o]

def bfs(n, g, v, q, s, dxs, dys, dest):
    while q:
        y, x, o = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, o, v, g):
                push(nx, ny, o, v, q, s, s[y][x][o][0] + 1 if o in s[y][x] else 1)

# 출발 지점에서 대피 장소까지 거리를 정리하는 함수
def init_dists(s, d, h, dest):
    for r, c in dest:
        for i in range(h):
            if i in s[r][c]:
                dist, who = s[r][c][i]
                d[who] = dist if d[who] == -1 else min(d[who], dist)

n, h, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]

# 사람이 서있는 위치를 시작점으로 사용하기 위해 별도의 리스트에 위치 정보 저장, 대피 공간의 위치를 도착점으로 사용하기 위해 위치 정보를 저장
human = []
dest = []
order = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            human.append([i, j, order])
            order += 1
        if grid[i][j] == 3: dest.append([i, j])

# 사람 수만큼 bfs를 실행하여 사람마다 비를 피할 공간으로 이동하는 최소 거리를 구한다.
q = deque()
visited = [[{} for _ in range(n)] for _ in range(n)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
for y, x, o in human:
    q.append([y, x, o])
    visited[y][x][o] = True

steps = [[{} for _ in range(n)] for _ in range(n)]
bfs(n, grid, visited, q, steps, dx, dy, dest)

# 생성된 거리 정보를 바탕으로 출발 지점에서 대피 장소까지 거리를 정리
dists = [-1 for _ in range(h)]
init_dists(steps, dists, h, dest)

h_idx = 0
for i in range(n):
    for j in range(n):
        if h_idx < h and i == human[h_idx][0] and j == human[h_idx][1]:
            print(dists[h_idx], end=' ')
            h_idx += 1
        else: print(0, end=' ')
    print()