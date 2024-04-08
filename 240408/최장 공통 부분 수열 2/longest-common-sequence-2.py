def in_range(i, j, n, m):
    return 0 < i < n and 0 < j < m

def init_dp(s1, s2):
    dp = [[[0, ''] for _ in range(len(s2))] for _ in range(len(s1))]
    return dp

s1 = ' ' + input()
s2 = ' ' + input()

# dp를 사용해 최장 공통 부분 수열의 길이와 부분 수열을 갱신하며 dp 테이블을 채운다.
dp = init_dp(s1, s2)
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j][0] = dp[i - 1][j - 1][0] + 1
            dp[i][j][1] = dp[i - 1][j - 1][1] + s1[i] 
        else:
            if dp[i - 1][j][0] >= dp[i][j - 1][0]:
                dp[i][j][0] = dp[i - 1][j][0]
                dp[i][j][1] = dp[i - 1][j][1]
            else:
                dp[i][j][0] = dp[i][j - 1][0]
                dp[i][j][1] = dp[i][j - 1][1]

# 두 문자열의 모든 문자를 검사한 결과인 dp[-1][-1][1]이 정답
print(dp[-1][-1][1])