def init_dp(n, f_info):
    dp = [[0 for _ in range(3)] for _ in range(n)]
    # dp의 첫번째 줄은 1층의 보물 정보로 초기화
    for i in range(3):
        dp[0][i] = f_info[i]
    return dp

n = int(input())
floor_info = [[int(x) for x in input().split()] for _ in range(n)]

# dp[i][j]으로 올 수 있는 방 중 직전까지 모든 보물의 최대값을 선택하는 dp
dp = init_dp(n, floor_info[0])
for i in range(1, n):
    # i층의 j번째 방이 선택할 수 있는 최대값을 탐색
    for j in range(3):
        for k in range(3):
            # 현재 선택한 방과 직전에 선택한 방이 같으면 무시
            if j == k:
                continue

            dp[i][j] = max(dp[i][j], dp[i - 1][k] + floor_info[i][j])

# n층의 최대값이 정답
print(max(dp[n - 1]))