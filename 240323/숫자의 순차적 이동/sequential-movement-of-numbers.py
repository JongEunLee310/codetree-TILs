def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

n, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]

# 각 숫자들의 위치를 dict에 저장 - 매 턴마다 숫자의 위치를 탐색하지 않기 위해
num_loc = {}
for i in range(n):
    for j in range(n):
        num_loc[grid[i][j]] = [i, j]

# 숫자 이동
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(m):
    for i in range(1, n * n + 1):
        r, c = num_loc[i]
        # 중심을 기준으로 인접한 수 중 최대값 탐색
        max_value = 0
        for j in range(8):
            nr, nc = r + dr[j], c + dc[j]
            if in_range(nr, nc, n, n):
                max_value = max(max_value, grid[nr][nc])

        # 최대값과 위치 변경
        grid[r][c], grid[num_loc[max_value][0]][num_loc[max_value][1]] = grid[num_loc[max_value][0]][num_loc[max_value][1]], grid[r][c]
        num_loc[i], num_loc[max_value] = num_loc[max_value], num_loc[i]

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()