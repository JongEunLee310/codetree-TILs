def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]
r, c = [int(x) - 1 for x in input().split()]

# 폭발 범위 안에 드는 영역을 0으로 처리
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
explode_range = grid[r][c]
grid[r][c] = 0
for i in range(4):
    for j in range(1, explode_range):
        nx, ny = c + dx[i] * j, r + dy[i] * j
        if in_range(nx, ny, n, n):
            grid[ny][nx] = 0

# 폭발 후 중력 작용 적용
for i in range(n):
    tmp = []
    for j in range(n):
        if grid[j][i] > 0:
            tmp.append(grid[j][i])
    
    for j in range(-1, -n - 1, -1):
        try:
            grid[j][i] = tmp[j]
        except:
            grid[j][i] = 0

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()