n = int(input())
dp = [0 for _ in range(n + 1)]

# i - k까지 채워져 있을 때
    # k = 1 : 한 열을 채우기 위한 방법은 1가지
    # k = 2 : 두 열을 채우기 위한 방법은 2가지
# 점화식 : dp[n] = dp[n - 1] * dp[n - 2] * 2
dp[0], dp[1] = 1, 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2
print(dp[n])