from collections import deque

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, nx, ny, v, g, u, d):
    if not in_range(nx, ny, len(g[0]), len(g)): return False
    
    diff = abs(g[y][x] - g[ny][nx])
    if v[ny][nx] == 1 or not (diff >= u and diff <= d): return False

    return True

def push(x, y, v, q):
    q.append([y, x])
    v[y][x] = 1

def bfs(n, g, v, q, dxs, dys, u, d):
    while q:
        y, x = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(x, y, nx, ny, v, g, u, d):
                push(nx, ny, v, q)

def get_max(n, k, g, q, city, dx, dy, u, d, l, idx):
    if len(l) == k:
        visited = [[0 for _ in range(n)] for _ in range(n)]
        for r, c in l:
            q.append([r, c])
            visited[r][c] = 1

        bfs(n, g, visited, q, dx, dy, u, d)
        
        result = 0
        for i in range(n):
            result += sum(visited[i])
        
        return result
    if idx >= len(city): return 0

    max_cities = 0
    # 현재 도시를 포함한 결과
    l.append(city[idx])
    r1 = get_max(n, k, g, q, city, dx, dy, u, d, l, idx + 1)
    l.pop()

    # 현재 도시를 제외한 결과
    r2 = get_max(n, k, g, q, city, dx, dy, u, d, l, idx + 1)

    max_cities = max(max_cities, r1, r2)

    return max_cities

n, k, u, d = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]
# city를 1차원 리스트로 저장
city = []
for i in range(n):
    for j in range(n):
        city.append([i, j])
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
q = deque()
print(get_max(n, k, grid, q, city, dx, dy, u, d, [], 0))