def init_dp(n, k):
    # j는 0 ~ k까지 고려할 것이므로 가장 왼쪽에 1칸 패딩을 주고 k + 1만큼 열을 가지게 한다.
    dp = [[0 for _ in range(k + 2)] for _ in range(n + 1)]
    return dp

n, k = [int(x) for x in input().split()]
string = input()

# 최대 k번까지 j번 움직였을 때 얻을 수 있는 최대 수정 구슬을 구한다.
    #  dp[i][j] = max(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1)
dp = init_dp(n, k)
for i in range(1, n + 1):
    loc = string[i - 1]
    for j in range(1, k + 2):
        # 움직인 횟수가 j번이고 홀수일 때는 위치가 L이고 짝수일 때는 R이다.
            # 현재 엘라의 위치가 L일 때
                # 현재 구슬의 위치가 L일 때는 직전의 위치에서 움직이지 않고 구슬을 1 추가하는 방법과 움직여서 구슬을 1 추가하는 방법 중 최대값을 선택
                # 현재 구슬의 위치가 R일 때는 직전의 위치에서 움직이지 않는 방법과 움직이는 방법 중 최대값을 선택
            # 현재 엘라의 위치가 R일 때
                # 현재 구슬의 위치가 R일 때는 직전의 위치에서 움직이지 않고 구슬을 1 추가하는 방법과 움직여서 구슬을 1 추가하는 방법 중 최대값을 선택
                # 현재 구슬의 위치가 L일 때는 직전의 위치에서 움직이지 않는 방법과 움직이는 방법 중 최대값을 선택
        if j % 2 != 0:
            dp[i][j] = max(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1) if loc == 'L' else max(dp[i - 1][j], dp[i - 1][j - 1])   
        else:
            dp[i][j] = max(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1) if loc == 'R' else max(dp[i - 1][j], dp[i - 1][j - 1])

# 수정이 n번 생성되었을 때 최대값이 정답
print(max(dp[n]))