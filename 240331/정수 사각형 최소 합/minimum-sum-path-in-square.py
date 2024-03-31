# 오른쪽 상단에서 왼쪽으로만 이동한 경우와 아래로만 이동한 경우를 dp 테이블에 초기화
def init_dp(n, g):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][-1] = grid[0][-1]
    for i in range(1, n):
        dp[i][-1] += (dp[i - 1][-1] + grid[i][-1])
        dp[0][-i - 1] += (dp[0][-i] + grid[0][-i - 1])
    return dp

N = int(input())
grid = [[int(x) for x in input().split()] for _ in range(N)]

dp = init_dp(N, grid)

# dp 테이블을 초기화 되지 않은 값들 중 오른쪽 상단부터 dp[i][j] = min(dp[i - 1][j], dp[i][j + 1]) + grid[i][j]를 점화식으로 채운다.
for i in range(1, N):
    for j in range(N - 2, -1, -1):
        dp[i][j] = min(dp[i - 1][j], dp[i][j + 1]) + grid[i][j]

print(dp[-1][0])