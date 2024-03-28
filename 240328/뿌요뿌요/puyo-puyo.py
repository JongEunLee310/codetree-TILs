def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def dfs(n, g, v, dx, dy, x, y, cur, size):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny, n, n) and not v[ny][nx] and g[ny][nx] == cur:
            visited[ny][nx] = True
            size = dfs(n, g, v, dx, dy, nx, ny, cur, size + 1)
    return size

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]

# 격자를 순회하면서 방문하지 않은 숫자가 있을 때 블럭의 크기 4이상의 블럭 수와 최대 블럭 크기를 구한다.
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
visited = [[False for _ in range(n)] for _ in range(n)]
blk, max_blk = 0, 0
cur = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cur = grid[i][j]
            visited[i][j] = True
            blk_size = dfs(n, grid, visited, dx, dy, j, i, cur, 1)
            if blk_size >= 4: blk += 1
            max_blk = max(max_blk, blk_size)

print(blk, max_blk)