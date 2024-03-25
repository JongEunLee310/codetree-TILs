def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

# 현재 위치에서 이동할 수 있는 모든 위치를 탐색해서 최대 움직임을 구하는 함수
def get_maximum_move(m, n, grid, dirs, dx, dy, r, c):
    if not is_possible_move(n, grid, dirs, dx, dy, r, c): return m

    max_move = m
    for i in range(1, n):
        nr, nc = r + dy[dirs[r][c]] * i, c + dx[dirs[r][c]] * i
        if in_range(nr, nc, n, n) and grid[nr][nc] > grid[r][c]:
            max_move = max(max_move, get_maximum_move(m + 1, n, grid, dirs, dx, dy, nr, nc))

    return max_move

# 현재 위치에서 이동할 수 있는 위치 여부를 판단
def is_possible_move(n, grid, dirs, dx, dy, r, c):
    result = False
    for i in range(1, n):
        nr, nc = r + dy[dirs[r][c]] * i, c + dx[dirs[r][c]] * i
        if in_range(nr, nc, n, n) and grid[nr][nc] > grid[r][c]:
            result = True
            break
    
    return result

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]
dirs = [[int(x) - 1 for x in input().split()] for _ in range(n)]
r, c = [int(x) - 1 for x in input().split()]
dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]

print(get_maximum_move(0, n, grid, dirs, dx, dy, r, c))