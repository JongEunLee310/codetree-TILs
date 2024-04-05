def init_dp(n):
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 0
    return dp

n = int(input())
c1 = [int(x) for x in input().split()]
c2 = [int(x) for x in input().split()]

# 우향, 하향, 우하향 방량으로 현재 최대값을 전달하는 방식의 dp
dp = init_dp(n)
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue
        
        # 카드 버리기
        dp[i + 1][j + 1] = dp[i][j]

        if c2[i] > c1[j]:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])
        elif c2[i] < c1[j]:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + c2[i])

ans = 0
for i in range(n + 1):
    ans = max(dp[i])
print(ans)