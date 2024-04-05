INF = 10 ** 9

# 음수가 k개까지 허용되는 dp 테이블 초기화
def init_dp(n):
    dp = [[-INF for _ in range(k + 1)] for _ in range(n + 1)]
    return dp

n, k = [int(x) for x in input().split()]
nums = [0] + [int(x) for x in input().split()]

# i번째 숫자를 마지막으로, 음수가 j번 나타났을 때 나타나는 연속합 중 최댓값을 dp[i][j]에 저장
dp = init_dp(n)
ans = -INF

for i in range(1, n + 1):
    if nums[i] >= 0:
        for j in range(k + 1):
            dp[i][j] = max(dp[i - 1][j] + nums[i], nums[i])
            ans = max(ans, dp[i][j])
    else:
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + nums[i], nums[i])
            ans = max(ans, dp[i][j])

print(ans)