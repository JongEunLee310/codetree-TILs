def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m 

def explode(grid, t):
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    dist = 2 ** (t - 1)

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != None and grid[i][j] < t:
                for k in range(4):
                    nx, ny = j + dx[k] * dist, i + dy[k] * dist
                    if in_range(nx, ny, len(grid), len(grid)) and grid[ny][nx] == None:
                        grid[ny][nx] = t

n, m, r, c = [int(x) for x in input().split()]
grid = [[None for _ in range(n)] for _ in range(n)]

grid[r - 1][c - 1] = 0
for i in range(1, m + 1):
    explode(grid, i)

cnt = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != None: cnt += 1

print(cnt)