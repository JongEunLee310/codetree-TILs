# 왼쪽 상단에서 오른쪽으로만 혹은 아래쪽으로만 이동하였을 때 경우를 dp 테이블에 초기화
def init_dp(n, g):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = g[0][0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], g[i][0])
        dp[0][i] = max(dp[0][i - 1], g[0][i])
    return dp

N = int(input())
grid = [[int(x) for x in input().split()] for _ in range(N)]

dp = init_dp(N, grid)

# 왼쪽과 위쪽의 dp 테이블 값 중 최솟값과 grid의 현재 값을 비교하여 큰 값을 dp[i][j]에 저장
for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(min(dp[i - 1][j], dp[i][j - 1]), grid[i][j])

print(dp[-1][-1])