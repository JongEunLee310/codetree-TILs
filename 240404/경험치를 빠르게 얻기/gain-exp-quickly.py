from sys import maxsize

n, m = [int(x) for x in input().split()]
q_info = [[int(x) for x in input().split()] for _ in range(n)]

# 경험치를 인덱스로 하는 dp 테이블을 사용하여 인덱스별 최소 시간을 저장
q_info.sort(key = lambda x : x[0])
dp = [maxsize for _ in range(m + 1)]
dp[0] = 0
for e, t in q_info:
    for i in range(m, 0, -1):
        if i - e >= 0:
            dp[i] = min(dp[i], dp[i - e] + t)
        else:
            dp[i] = min(dp[i], t)

print(dp[-1])