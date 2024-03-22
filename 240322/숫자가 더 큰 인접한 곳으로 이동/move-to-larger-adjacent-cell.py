def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

n, r, c = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]

r, c = r - 1, c - 1
print(grid[r][c], end=' ')
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
while True:
    not_found = 0
    for i in range(4):
        nx, ny = c + dx[i], r + dy[i]
        if in_range(nx, ny, n, n) and grid[ny][nx] > grid[r][c]:
            c, r = nx, ny
            print(grid[r][c], end=' ')
            break
        not_found += 1
    if not_found == 4: break