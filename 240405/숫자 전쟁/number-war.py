from sys import maxsize

def init_dp(n):
    dp = [[-maxsize for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
        dp[0][i] = 0
    return dp

n = int(input())
c1 = [int(x) for x in input().split()]
c2 = [int(x) for x in input().split()]

dp = init_dp(n)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if c2[i - 1] > c1[j - 1]:
            dp[i][j] = dp[i][j - 1]
        elif c2[i - 1] < c1[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + c2[i - 1])
        else:
            dp[i][j] = dp[i - 1][j - 1]

ans = 0
for i in range(n + 1):
    ans = max(dp[i])
print(ans)