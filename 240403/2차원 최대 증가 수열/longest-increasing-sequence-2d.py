n, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]

dp =[[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1
for i in range(1, n):
    for j in range(1, m):
        for k in range(i):
            for l in range(j):
                if grid[i][j] > grid[k][l] and dp[k][l] > 0:
                    dp[i][j] = max(dp[i][j], dp[k][l] + 1)

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])
print(ans)