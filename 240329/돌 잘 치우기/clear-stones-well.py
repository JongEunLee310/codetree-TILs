from collections import deque

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, v, g):
    if not in_range(x, y, len(g[0]), len(g)): return False
    if v[y][x] == 1 or g[y][x] == 1: return False

    return True

def push(x, y, v, q):
    q.append([y, x])
    v[y][x] = 1

def bfs(n, g, v, q, dxs, dys):
    while q:
        y, x = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, v, g):
                push(nx, ny, v, q)

# 재귀적으로 m개의 돌을 선택해 bfs를 실행하는 함수
def get_max(n, m, g, stones, s_idx, cnt, starts, q, dx, dy):
    if cnt == m:
        for s in starts:
            q.append(s)
        #실행 후 도달가능한 칸의 수 계산
        visited = [[0 for _ in range(len(g[0]))] for _ in range(len(g))]
        
        bfs(n, g, visited, q, dx, dy)
        result = 0        
        for i in range(len(visited)):
            result += sum(visited[i])

        return result
    if s_idx >= len(stones): return 0

    max_area = 0
    # 현재 돌을 선택하는 방법
    r, c = stones[s_idx]
    g[r][c] = 0
    
    r1 = get_max(n, m, g, stones, s_idx + 1, cnt + 1, starts, q, dx, dy)
    g[r][c] = 1

    # 현재 돌을 선택하지 않는 방법
    r2 = get_max(n, m, g, stones, s_idx + 1, cnt, starts, q, dx, dy)

    max_area = max(max_area, r1, r2)

    return max_area

n, k, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]
starts = [[int(x) - 1 for x in input().split()] for _ in range(k)]
stones = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1: stones.append([i, j])

q = deque()
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
print(get_max(n, m, grid, stones, 0, 0, starts, q, dx, dy))