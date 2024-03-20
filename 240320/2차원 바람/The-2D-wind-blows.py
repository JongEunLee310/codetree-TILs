def move_right(r1, c1, c2, grid):
    for i in range(c2, c1 - 1, -1):
        grid[r1][i] = grid[r1][i - 1]

def move_left(r2, c1, c2, grid, right_tmp):
    for i in range(c1, c2 - 1):
        grid[r2][i] = grid[r2][i + 1]
    grid[r2][c2 - 1] = right_tmp

def move_up(r1, r2, c1, grid, lower_tmp):
    for i in range(r1, r2 - 1):
        grid[i][c1] = grid[i + 1][c1]
    grid[r2 - 1][c1] = lower_tmp

def move_down(r1, r2, c2, grid, upper_tmp):
    for i in range(r2, r1 + 1, -1):
        grid[i][c2] = grid[i - 1][c2]
    grid[r1 + 1][c2] = upper_tmp

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def change_value(r1, c1, r2, c2, grid, N, M):
    average = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]

    di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            num_sum = grid[i][j]
            num_cnt = 1
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if in_range(ni, nj, N, M):
                    num_sum += grid[ni][nj]
                    num_cnt += 1
            average[i - r1][j - c1] = num_sum // num_cnt

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            grid[i][j] = average[i - r1][j - c1]



N, M, Q = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(N)]
w_info = [[int(x) for x in input().split()] for _ in range(Q)]

for i in range(Q):
    r1, c1, r2, c2 = [x - 1 for x in w_info[i]]

    # 직사각형 경계 이동
    upper_tmp, right_tmp, lower_tmp = grid[r1][c2], grid[r2][c2], grid[r2][c1]
    move_right(r1, c1, c2, grid)
    move_down(r1, r2, c2, grid, upper_tmp)
    move_left(r2, c1, c2, grid, right_tmp)
    move_up(r1, r2, c1, grid, lower_tmp)

    # 직사각형 영역 내 각각의 블록의 값을 블록 주변의 평균값으로 변경
    change_value(r1, c1, r2, c2, grid, N, M)

for i in range(N):
    for j in range(M):
        print(grid[i][j], end=' ')
    print()