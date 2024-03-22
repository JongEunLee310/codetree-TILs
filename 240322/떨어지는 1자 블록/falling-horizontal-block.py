def in_range(x, n):
    return 0 <= x < n

n, m, k = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    stop_loc = False
    # 블럭 좌우에 붙은 블럭이 있는지 검사
    if in_range(k - 2, n) and grid[i][k - 2] == 1 or in_range(k + m, n) and grid[i][k + m] == 1:
        stop_loc = i

    # 블럭 아래에 붙은 블럭이 있는지 검사
    if i + 1 < n and not stop_loc:
        for j in range(k - 1, k + m - 1):
            if grid[i + 1][j] == 1:
                stop_loc = i
                break
    
    # 블럭이 가장 아래칸까지 내려왔을 경우
    if stop_loc != False or not stop_loc and i + 1 == n:
        for j in range(k - 1, k + m - 1):
            grid[i][j] = 1
        break

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()