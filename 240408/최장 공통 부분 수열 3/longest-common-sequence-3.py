def init_dp(n, m):
    dp = [[[0, []] for _ in range(m + 1)] for _ in range(n + 1)]
    return dp

# dp[i - 1][j]의 길이와 dp[i][j - 1]의 길이가 같을 때 사전 순으로 더 빠른 수열을 반환
def choose_head(s1, s2):
    if len(s1) == 0:
        return []

    # 같은 인덱스에서 더 빠른 값이 있다면 그 수열을 반환
    for i in range(len(s1)):
        if s1[i] < s2[i]:
            return s1
        elif s1[i] > s2[i]:
            return s2
    # 두 수열이 동일하면 아무거나 반환
    return s1

n, m = [int(x) for x in input().split()]
a = [0] + [int(x) for x in input().split()] 
b = [0] + [int(x) for x in input().split()]

# dp를 사용해 최장 공통 부분 수열의 길이와 부분 수열을 갱신하며 dp 테이블을 채운다.
dp = init_dp(n, m)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i] == b[j]:
            dp[i][j][0] = dp[i - 1][j - 1][0] + 1
            dp[i][j][1] = dp[i - 1][j - 1][1] + [a[i]] 
        else:
            if dp[i - 1][j][0] > dp[i][j - 1][0]:
                dp[i][j][0] = dp[i - 1][j][0]
                dp[i][j][1] = dp[i - 1][j][1]
            elif dp[i - 1][j][0] < dp[i][j - 1][0]:
                dp[i][j][0] = dp[i][j - 1][0]
                dp[i][j][1] = dp[i][j - 1][1]
            # dp[i - 1][j]와 dp[i][j - 1]의 길이가 같을 때 사전 순으로 더 빠른 수열을 dp[i][j]에 저장
            elif dp[i - 1][j][0] == dp[i][j - 1][0]:
                dp[i][j][0] = dp[i - 1][j][0]
                dp[i][j][1] = choose_head(dp[i - 1][j][1], dp[i][j - 1][1])

# 두 문자열의 모든 문자를 검사한 결과인 dp[-1][-1][1]이 정답
for i in range(dp[-1][-1][0]):
    print(dp[-1][-1][1][i], end=' ')