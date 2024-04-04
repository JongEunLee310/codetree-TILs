from sys import maxsize

N, M = [int(x) for x in input().split()]
j_info = [[int(x) for x in input().split()] for _ in range(N)]

# 보석의 무게 합을 인덱스로 사용하는 dp 테이블을 사용하고 각 인덱스별 최대 가치를 저장
#보석 정보를 무게를 기준으로 정렬
j_info.sort(key = lambda x : x[0])
dp = [-maxsize for _ in range(M + 1)]
dp[0] = 0
for i in range(1, M + 1):
    for w, v in j_info:
        if i - w >= 0:
            dp[i] = max(dp[i], dp[i - w] + v)
# dp 테이블의 최대값을 출력
print(max(dp))