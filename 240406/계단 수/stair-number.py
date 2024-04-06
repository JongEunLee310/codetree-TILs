def init_dp(n):
    dp = [[0 for _ in range(10)] for _ in range(n + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    return dp

n = int(input())

# dp[i][j]에서 갈 수 있는 숫자의 dp 테이블에 dp[i][j]를 더해주는 dp 테이블
    # dp[i][j]에서 갈 수 있는 다음 dp테이블
        # dp[i + 1][j - 1], dp[i + 1][j + 1]
dp = init_dp(n)
for i in range(1, n):
    for j in range(10):
        # j + 1이 9보다 크지 않을 때
        if j + 1 <= 9:
            dp[i + 1][j + 1] += dp[i][j]
        
        # j - 1이 0보다 작지 않을 때
        if j - 1 >= 0:
            dp[i + 1][j - 1] += dp[i][j]

# dp[n]의 모든 값을 더한 값에 1000000007을 나눈 나머지가 정답
print(sum(dp[n]) % 1000000007)