def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

n, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]

# L모양 블럭의 최대값
b1, b2 = [[1, 0], [0, -1], [-1, 0], [0, 1]], [[1, 1], [1, -1], [-1, -1], [-1, 1]]
max_L = 0
for i in range(n):
    for j in range(m):
        # 기본 L모양
        for k in range(4):
            if in_range(i + b1[k][0], j + b1[k][1], n, m) and in_range(i + b2[k][0], j + b2[k][1], n, m):
                L = grid[i][j] + grid[i + b1[k][0]][j + b1[k][1]] + grid[i + b2[k][0]][j + b2[k][1]]
                max_L = max(max_L, L)
        # 뒤집힌 L모양
        for k in range(4):
            if in_range(i + b1[k][0], j + b1[k][1], n, m) and in_range(i + b2[(k + 1) % 4][0], j + b2[(k + 1) % 4][1], n, m):
                L = grid[i][j] + grid[i + b1[k][0]][j + b1[k][1]] + grid[i + b2[(k + 1) % 4][0]][j + b2[(k + 1) % 4][1]]
                max_L = max(max_L, L)

# bar 모양 블럭의 최대값
max_bar = 0
for i in range(n):
    for j in range(m):
        # 가로 방향 bar
        hor_bar = 0
        for k in range(j, j + 3):
            if not in_range(i, k, n, m):
                hor_bar = 0
                break
            hor_bar += grid[i][k]
        
        # 세로 방향 bar
        ver_bar = 0
        for k in range(i, i + 3):
            if not in_range(k, j, n, m):
                ver_bar = 0
                break
            ver_bar += grid[k][j]

        max_bar = max(max_bar, hor_bar, ver_bar)

print(max(max_L, max_bar))