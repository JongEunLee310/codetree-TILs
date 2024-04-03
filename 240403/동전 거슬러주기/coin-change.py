from sys import maxsize

N, M = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]

# 현재 동전 합을 만들 수 있는 최소 동전 개수를 구하는 DP, 동전의 값만큼 이전의 dp의 값을 더한 것 중 최솟값을 dp[i]에 저장
dp = [maxsize for _ in range(M + 1)]
dp[0] = 0
for i in range(1, M + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)
print(dp[-1])