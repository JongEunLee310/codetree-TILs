import copy

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def explode(grid, r, c):
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

def get_pair(grid):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                for k in range(4):
                    nx, ny = j + dx[k], i + dy[k]
                    if in_range(nx, ny, len(grid), len(grid)) and grid[i][j] == grid[ny][nx]:
                        cnt += 1
    
    return cnt // 2

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]

max_pair = 0
for i in range(n):
    for j in range(n):
        new_grid = copy.deepcopy(grid)
        explode(new_grid, i, j)
        pair = get_pair(new_grid)
        max_pair = max(max_pair, pair)

print(max_pair)