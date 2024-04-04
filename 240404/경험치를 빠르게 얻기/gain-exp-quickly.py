from sys import maxsize

# 퀘스트 수행시간별 최대 경험치를 구하는 dp이므로 -maxsize로 초기화, 퀘스트 개수와 시간을 고려한 dp 테이블
def init_dp(n, t):
    dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(t + 1):
            dp[i][j] = -maxsize
    dp[0][0] = 0
    
    return dp

n, m = [int(x) for x in input().split()]
q_info = [[int(x) for x in input().split()] for _ in range(n)]

# 최대 수행시간 계산
t = 0
for qe, qt in q_info:
    t += qt

# dp 초기화
dp = init_dp(n, t)

for i in range(1, n + 1):
    for j in range(t + 1):
        # 현재 퀘스트를 포함할 때 최대 경험치
            # 현재 퀘스트를 포함하기 위해 i - 1번째 퀘스트 수행 시간이 j - q_info[i][1]가 되어야 한다. 
        if j - q_info[i - 1][1] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - q_info[i - 1][1]] + q_info[i - 1][0])
        
        # 현재 퀘스트를 포함하지 않는 최대 경험치
            # 현재 퀘스트를 포함하지 않아 i - 1번째 퀘스트 수행 시간이 j가 되어야 한다.
        dp[i][j] = max(dp[i][j], dp[i - 1][j])

# n개의 퀘스트를 고려했을 때 최대 경험치 합이 m 이상인 경우 중 최소 시간을 계산
ans = maxsize
for j in range(t + 1):
    if dp[n][j] >= m:
        ans = min(ans, j)

print(ans if ans > -maxsize else -1)