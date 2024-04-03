def in_range(a1, a2):
    return a1[0] <= a2[0] <= a1[1] or a1[0] <= a2[1] <= a1[1] or a2[0] <= a1[0] <= a2[1] or a2[0] <= a1[1] <= a2[1]

# dp 테이블을 해당 인덱스의 알바만 했을 때 급여로 초기화
def init_dp(a):
    return [a[i][2] for i in range(len(a))]

N = int(input())
alba = [[int(x) for x in input().split()] for _ in range(N)]
alba.sort(key = lambda x : [x[1], x[2]])
dp = init_dp(alba)

# 이전 시간대 앏바와 시간이 겹치지 않는 알바 중 최대에 현재 시간대 알바 급여를 더한다.
for i in range(N):
    for j in range(i):
        if not in_range(alba[i], alba[j]):
            dp[i] = max(dp[i], dp[j] + alba[i][2])

# dp 테이블의 최대값이 정답
print(max(dp))