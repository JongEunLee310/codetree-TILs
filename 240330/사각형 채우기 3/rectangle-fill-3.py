MOD = 1000000007

def fill(n, dp):
    dp[0] = 1
    dp[1] = 2

    # i - k까지 채워져 있을 때
        # k = 1 : 남은 한 열을 채우는 방법은 2가지
        # k = 2 : 남은 두 열을 채우는 방법은 3가지
        # k >= 3: 남은 k열을 채우는 경우는 2가지
    # 점화식 : dp[i] = 2 * dp[i - 1] + 3 * dp[i - 2] + 2 * (dp[i - 3] + dp[i - 4] + ... + dp[1] + dp[0])
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3) % MOD

        for j in range(i - 3, -1, -1):
            dp[i] = (dp[i] + dp[j] * 2) % MOD
    
    return dp[n]

n = int(input())
dp = [0 for _ in range(n + 1)]
print(fill(n, dp))