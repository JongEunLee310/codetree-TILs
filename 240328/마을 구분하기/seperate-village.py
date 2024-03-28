def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

# 현재 위치에서 4방향으로 dfs 탐색해서 마을의 사람 수를 구하는 함수
def dfs(n, grid, visited, dx, dy, x, y, p):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny, n, n) and grid[ny][nx] == 1 and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            p = dfs(n, grid, visited, dx, dy, nx, ny, p + 1)
    
    return p

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

# 격자의 왼쪽 상단부터 오른쪽 하단까지 순회하면서 사람이고 방문하지 않은 상태이면 dfs를 실행하여 마을에 있는 사람의 수를 구함
cnt = 0
p = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            visited[i][j] = 1
            p.append(dfs(n, grid, visited, dx, dy, j, i, 1))
p.sort()

print(cnt)
for i in range(len(p)):
    print(p[i])