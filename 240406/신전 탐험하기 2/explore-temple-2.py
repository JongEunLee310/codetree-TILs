def init_dp(n, f_info):
    # 1층에서 선택한 방에서 출발하는 경우로 나눠 초기화 dp[0] = 왼쪽, dp[1] = 가운데, dp[2] = 오른쪽에서 출발
    dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(3)]
    # dp의 첫번째 줄은 1층의 보물 정보로 초기화
    for i in range(3):
        dp[i][0][i] = f_info[i]
    return dp

n = int(input())
floor_info = [[int(x) for x in input().split()] for _ in range(n)]

# 1층에서 왼쪽, 중간, 오른쪽에서 출발하는 경우 세가지로 나눈다.
# dp[i][j]으로 올 수 있는 방 중 직전까지 모든 보물의 최대값을 선택하는 dp
dp = init_dp(n, floor_info[0])

for s in range(3):
    # 1층의 s번째 방에서 출발하는 경우의 dp 테이블을 채움
    for i in range(1, n):
        # i층의 j번째 방이 선택할 수 있는 최대값을 탐색
        for j in range(3):
            for k in range(3):
                # 현재 선택한 방과 직전에 선택한 방이 같으면 무시
                if j == k or i == n - 1 and j == s:
                    continue

                dp[s][i][j] = max(dp[s][i][j], dp[s][i - 1][k] + floor_info[i][j])

# 서로 다른 방에서 출발한 경우에서 n층의 값 중 1층에서 선택한 방과 n층에서 선택한 방의 위치가 다른 것 중 최대값이 정답
ans = 0
for i in range(3):
    ans = max(ans, max(dp[i][-1]))

print(ans)