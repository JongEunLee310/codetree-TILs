from collections import deque

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, v, g):
    if not in_range(x, y, len(g[0]), len(g)): return False
    if v[y][x] or g[y][x] == 1: return False

    return True

def push(x, y, v, q):
    q.append([y, x])
    v[y][x] = True

# bfs를 사용해서 시작점으로부터 갈 수 있는 지점의 개수를 구하는 함수
def bfs(g, v, dxs, dys, q):
    cnt = 0
    while q:
        cur_y, cur_x = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy
            if can_go(nx, ny, v, g):
                push(nx, ny, v, q)


n, k = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]
starts = [[int(x) - 1 for x in input().split()] for _ in range(k)]

# 모든 시작점에서 도달할 수 있는 지점을 방문한 여부를 저장하는 리스트
total_visited = [[0 for _ in range(n)] for _ in range(n)]

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

# 시작점의 개수만큼 bfs 실행
for r, c in starts:
    # 방문 여부를 저장하는 visited 리스트 초기화
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[r][c] = True

    q = deque()
    q.append([r, c])
    
    bfs(grid, visited, dx, dy, q)

    for i in range(n):
        for j in range(n):
            if visited[i][j]: total_visited[i][j] = 1

result = 0
for i in range(n):
    result += sum(total_visited[i])
print(result)