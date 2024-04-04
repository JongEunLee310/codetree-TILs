from sys import maxsize

n = int(input())
profit = [int(x) for x in input().split()]

# 길이의 합을 인덱스로 사용하는 dp 테이블로 인덱스별 최대 수익을 저장
dp = [-maxsize for _ in range(n + 1)]
dp[0] = 0
for i in range(1, n + 1):
    for j in range(n):
        if i - j - 1 >= 0:
            dp[i] = max(dp[i], dp[i - j - 1] + profit[j])

print(max(dp))