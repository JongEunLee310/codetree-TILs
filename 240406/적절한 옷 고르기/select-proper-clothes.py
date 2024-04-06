def in_range(s, e, d):
    return s <= d <= e

def init_dp(n, m, c):
    dp = [[-1 for _ in range(n)] for _ in range(M + 1)]
    for i in range(n):
        if c[i][0] == 1:
            dp[1][i] = 0
    return dp

N, M = [int(x) for x in input().split()]
clothes = [[int(x) for x in input().split()] for _ in range(N)]

# 전날 입은 옷의 종류에 따라 만족도를 계산하는 dp
dp = init_dp(N, M, clothes)
for i in range(2, M + 1):
    for j in range(N):
        s, e, v = clothes[j]

        # 현재 선택한 옷을 오늘 입을 수 없으면 통과
        if not in_range(s, e, i):
            continue
        
        # 전날 입은 옷 중 만족도(|전일 화려함 - 금일 화려함|)가 가장 큰 값을 dp[i][j]에 저장
        for k in range(N):
            # 선택한 옷이 전날 입지 않았으면 통과
            if dp[i - 1][k] == -1:
                continue
            
            _, _, y_v = clothes[k]
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(y_v - v))

# M번째 일의 최대 만족감이 정답
print(max(dp[M]))