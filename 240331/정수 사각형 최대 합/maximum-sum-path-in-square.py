N = int(input())
grid = [[int(x) for x in input().split()] for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

# DP 테이블 초기화
dp[0][0] = grid[0][0]
for i in range(1, N):
    dp[i][0] += (dp[i - 1][0] + grid[i][0])
    dp[0][i] += (dp[0][i - 1] + grid[0][i])

# 행이나 열이 0이 아닌 칸부터는 dp[i][j] = max(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])인 점화식을 사용하여 채운다.
for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])

# 마지막 행에 있는 값 중 최대값을 선택
print(max(dp[-1]))