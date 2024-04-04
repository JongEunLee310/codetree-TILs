from sys import maxsize

N, M = [int(x) for x in input().split()]
j_info = [[int(x) for x in input().split()] for _ in range(N)]

# 무게를 합을 인덱스로 사용하는 dp 테이블로 각 인덱스별로 만들 수 있는 최대 가치를 저장, 입력된 보석 정보를 무게를 기준으로 오름차순 정렬
j_info.sort(key = lambda x : x[0])
dp = [-maxsize for _ in range(M + 1)]
dp[0] = 0
for w, v in j_info:
    for i in range(M, 0, -1):
        if i - w >= 0:
            dp[i] = max(dp[i], dp[i - w] + v)

print(max(dp))