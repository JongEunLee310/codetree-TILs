def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

N = int(input())
grid = [[int(x) for x in input().split()] for _ in range(N)]

max_coin = 0
for i in range(N):
    for j in range(N):
        coin = 0
        for k in range(i, i + 3):
            for l in range(j, j + 3):
                if in_range(k, l, N, N) and grid[k][l] == 1:
                    coin += 1
        max_coin = max(max_coin, coin)
print(max_coin)