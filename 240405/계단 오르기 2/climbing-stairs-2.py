from sys import maxsize

def init_dp(n, c):
    dp = [[-maxsize for _ in range(4)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = dp[i - 2][0] + coins[i - 1] if i % 2 == 0 and i >= 2 else 0
    return dp

n = int(input())
coins = [int(x) for x in input().split()]

# n층까지 1계단 오르는 것을 3번 이내로 수행한 경우을 고려
    # dp[i - 2][j] + coins[i]과 dp[i - 1][j - 1] + coins[i] 중 최대값을 dp[i][j]에 저장
dp = init_dp(n, coins)
for i in range(1, n + 1):
    for j in range(1, min(4, i + 1)):
        dp[i][j] = max(dp[i][j], dp[i - 2][j] + coins[i - 1], dp[i - 1][j - 1] + coins[i - 1]) if i - j >= 2 else max(dp[i][j], dp[i - 1][j - 1] + coins[i - 1])

print(max(dp[n]))