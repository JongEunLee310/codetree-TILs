def in_range(x, n):
    return 0 <= x < n

n, m, k = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]

stop = False
for i in range(n):
    # 블럭 아래에 붙은 블럭이 있는지 검사
    if i + 1 < n:
        for j in range(k - 1, k + m - 1):
            if grid[i + 1][j] == 1:
                stop = True
                break
    
    # 정지위치가 정해졌거나 블럭이 바닥까지 내려왔을 경우 블럭을 격자에 위치를 확정
    if stop or not stop and i + 1 == n:
        for j in range(k - 1, k + m - 1):
            grid[i][j] = 1
        break

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()