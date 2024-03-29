from collections import deque

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, v, g):
    if not in_range(x, y, len(g[0]), len(g)): return False
    if v[y][x] or g[y][x] == 0: return False

    return True

def push(x, y, v, q, steps, dist):
    q.append([y, x])
    v[y][x] = True
    steps[y][x] = dist

def bfs(g, v, q, steps, dxs, dys):
    while q:
        y, x = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, v, g):
                push(nx, ny, v, q, steps, steps[y][x] + 1)
    
    return steps[-1][-1] if steps[-1][-1] != 0 else -1

n, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True
steps = [[0 for _ in range(m)] for _ in range(n)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
q = deque()
q.append([0, 0])
print(bfs(grid, visited, q, steps, dx, dy))