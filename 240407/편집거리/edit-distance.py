def init_dp(s1, s2):
    dp = [[0 for _ in range(s2)] for _ in range(s1)]
    for i in range(s1):
        dp[i][0] = i
    for j in range(s2):
        dp[0][j] = j
    return dp

s1 = ' ' + input()
s2 = ' ' + input()

# 편집하는 행동의 최소값을 dp[i][j]
    # A의 i번째와 B의 j번째 글자가 다를 때
        # A의 글자를 삭제하거나 B에 삽입할 때는 i - 1번째 글자와 j번째 글자까지의 편집거리는 동일
            # dp[i - 1][j]
        # A에 글자를 삽입하거나 B의 글자를 삭제할 때는 i번째 글자와 j - 1번째 글자까지의 편집거리는 동일
            # dp[i][j - 1]
        # A의 i번째 글자를 B의 j번째 글자로 교환할 때는 i - 1번째 글자와 j - 1번째 글자까지의 편집거리는 동일
            # dp[i - 1][j - 1]
        # 위 세가지 경우 중 최소값에 1을 더한다.
    # A의 i번째와 B의 j번째 글자가 같을 때
        # dp[i][j] = dp[i - 1][j - 1] + 1
dp = init_dp(len(s1), len(s2))
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        dp[i][j] = dp[i - 1][j - 1] if s1[i] == s2[j] else min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

print(dp[len(s1) - 1][len(s2) - 1])