from collections import deque

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, v, g):
    if not in_range(x, y, len(g[0]), len(g)): return False
    if v[y][x] or g[y][x] == 0: return False

    return True

def push(x, y, q, v):
    q.append([y, x])
    v[y][x] = True

# bfs를 사용해서 탈출 가능한 경로 존재 여부를 판단하는 함수
def bfs(n, m, g, v, q, dxs, dys):
    result = 0
    while q:
        cur_y, cur_x = q.popleft()
        if cur_y == n - 1 and cur_x == m - 1:
            result = 1
            break

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy
            if can_go(nx, ny, v, g):
                push(nx, ny, q, v)

    return result

n, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
q = deque()
q.append([0, 0])
print(bfs(n, m, grid, visited, q, dx, dy))