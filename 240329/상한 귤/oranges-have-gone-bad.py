from collections import deque

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, v, g):
    if not in_range(x, y, len(g[0]), len(g)): return False
    if v[y][x] or g[y][x] == 0: return False

    return True

def push(x, y, v, q, s, dist):
    q.append([y, x])
    v[y][x] = True
    s[y][x] = dist

def bfs(g, v, q, s, dxs, dys):
    while q:
        y, x = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, v, g):
                push(nx, ny, v, q, s, s[y][x] + 1)

n, k = [int(x) for x in input().split()]
box = [[int(x) for x in input().split()] for _ in range(n)]

steps = [[-1 for _ in range(n)] for _ in range(n)]
# box내 썩은 귤의 위치로 큐와 visited, steps 리스트 초기화
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if box[i][j] == 2:
            q.append([i, j])
            visited[i][j] = True
            steps[i][j] = 0

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
bfs(box, visited, q, steps, dx, dy)

for i in range(n):
    for j in range(n):
        print(-2 if steps[i][j] == -1 and box[i][j] == 1 else steps[i][j], end=' ')
    print()