def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < n

# 격자 내 값을 별도의 리스트에 저장하고 정렬하여 크기가 작은 칸부터 dp를 수행할 수 있도록 한다.
def init_cell(n, g):
    cell = []
    for i in range(n):
        for j in range(n):
            cell.append([g[i][j], i, j])
    return sorted(cell, key = lambda x : x[0])

# 시작점부터 밟은 칸을 세기 때문에 모두 1로 초기화
def init_dp(n, g):
    dp = [[1 for _ in range(n)] for _ in range(n)]
    return dp

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]

cell = init_cell(n, grid)
dp = init_dp(n, grid)

# 현재 검사하는 칸에 인접한 칸 중 현재 칸의 값보다 큰 칸 중 최대값에 현재 거리에 1 더해준다. 혹은 현재 거리에 1 더해준 값보다 인접한 칸의 dp 테이블 값이 더 크다면 갱신하지 않는다.
dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
for v, y, x in cell:
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny, n, n) and grid[ny][nx] > grid[y][x]:
            dp[ny][nx] = max(dp[ny][nx], dp[y][x] + 1)

max_dist = 0
for i in range(n):
    for j in range(n):
        max_dist = max(max_dist, dp[i][j])
print(max_dist)