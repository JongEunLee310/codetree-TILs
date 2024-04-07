def init_dp(s1, s2):
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    return dp

s1 = input()
s2 = input()

# dp[i][j]는 첫번째 문자열을 i번째 문자까지 고려하고 두번째 문자열을 j번째 문자까지 고려했을 때 가능한 최장 공통 길이
dp = init_dp(s1, s2)
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# dp[len(s1)][len(s2)]가 정답
print(dp[len(s1)][len(s2)])