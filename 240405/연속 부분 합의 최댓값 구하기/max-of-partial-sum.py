from sys import maxsize

def init_dp(n):
    dp = [-maxsize for _ in range(n + 1)]
    return dp

n = int(input())
arr = [int(x) for x in input().split()]

# i - 1번째 합 + i번째 원소와 i번째 원소 * 2 중 최대값을 dp[i]에 저장
dp = init_dp(n)
for i in range(1, n + 1):
    dp[i] = max(dp[i - 1] + arr[i - 1], arr[i - 1])

print(max(dp))