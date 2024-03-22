def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def escape(grid, d, y, x):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    t = 0
    while True:
        t += 1
        x, y = x + dx[d], y + dy[d]
        if not in_range(x, y, len(grid), len(grid)):
            return t
        
        if grid[y][x] == 1:
            if d == 0 or d == 2:
                d = (d + 3) % 4
            else:
                d = (d + 1) % 4
        elif grid[y][x] == 2:
            if d == 0 or d == 2:
                d = (d + 1) % 4
            else:
                d = (d + 3) % 4

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]

# 모든 진입점을 완전 탐색해서 최대 탈출 시간 탐색
max_t = 0
for j in range(n):
    # 진입 방향이 가로 방향일 때 최대 시간
    t1 = escape(grid, 0, j, -1)
    t2 = escape(grid, 2, j, n)

    # 진입 방향이 세로 방향일 때 최대 시간
    t3 = escape(grid, 1, -1, j)
    t4 = escape(grid, 3, n, j)

    max_t = max(max_t, t1, t2, t3, t4)

print(max_t)