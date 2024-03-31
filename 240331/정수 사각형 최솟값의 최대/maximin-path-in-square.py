# 왼쪽 상단에서 오른쪽으로만 이동한 경로와 아래쪽으로만 이동한 경로 중 최소값이 저장되도록 초기화
def init_dp(n, g):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = g[0][0]
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][0], g[i][0])
        dp[0][i] = min(dp[0][i - 1], g[0][i])
    return dp

N = int(input())
grid = [[int(x) for x in input().split()] for _ in range(N)]

# 오른쪽 혹은 아래로만 이동하는 경로상 최소값 중 최대값을 dp[i][j]의 값으로 사용
dp = init_dp(N, grid)
for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = min(max(dp[i - 1][j], dp[i][j - 1]), grid[i][j])

print(dp[-1][-1])