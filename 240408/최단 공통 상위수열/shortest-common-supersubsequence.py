def init_dp(s, t):
    dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
    # dp[1][1]은 s[1] == t[1]일 때는 같은 문자 하나만 사용하면 되므로 1이고 다르면 두 문자 모두 가져와야 하므로 2가 된다.
    dp[1][1] = 1 if s[1] == t[1] else 2

    # s[i]가 t[1]과 같을 때는 s수열의 첫번째부터 i번째까지 문자만 가져오면 되므로 길이가 i가 된다.
    # s[i]가 t[1]과 다를 때는 dp[i - 1][1]이 직전 선택 중 가장 짧기 때문에 1 더해준 값을 dp[i][1]에 저장
    for i in range(2, len(s)):
        dp[i][1] = i if s[i] == t[1] else dp[i - 1][1] + 1

    # s[1]가 t[j]와 같을 때는 s수열의 첫번째부터 i번째까지 문자만 가져오면 되므로 길이가 i가 된다.
    # s[1]가 t[j]와 다를 때는 dp[1][j - 1]이 직전 선택 중 가장 짧기 때문에 1 더해준 값을 dp[1][j]에 저장
    for j in range(2, len(t)):
        dp[1][j] = j if t[j] == s[1] else dp[1][j - 1] + 1
    
    return dp

s = ' ' + input()
t = ' ' + input()

# s[i] == t[j]일 때
    # dp[i][j] = dp[i - 1][j - 1] + 1
# s[i] != t[j]일 때
    # dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
dp = init_dp(s, t)
for i in range(2, len(s)):
    for j in range(2, len(t)):
        dp[i][j] = dp[i - 1][j - 1] + 1 if s[i] == t[j] else min(dp[i - 1][j], dp[i][j - 1]) + 1

# dp[-1][-1]의 값이 정답
print(dp[-1][-1])