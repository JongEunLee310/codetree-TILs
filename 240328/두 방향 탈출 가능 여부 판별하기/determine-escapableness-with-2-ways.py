def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def dfs(m, n, grid, visited, dx, dy, x, y):
    if x == m - 1 and y == n - 1: return 1

    result = 0
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny, m, n) and grid[ny][nx] == 1 and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            result = dfs(m, n, grid, visited, dx, dy, nx, ny)
            visited[ny][nx] = 0
        if result == 1: break
    
    return result

n, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1
dx, dy = [0, 1], [1, 0]
print(dfs(m, n, grid, visited, dx, dy, 0, 0))