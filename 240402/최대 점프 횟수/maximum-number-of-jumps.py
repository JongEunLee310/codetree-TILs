n = int(input())
nums = [int(x) for x in input().split()]

dp = [-1 for _ in range(n)]
dp[0] = 0
for i in range(1, n):
    for j in range(i):
        if dp[j] == -1: continue

        if nums[j] >= i - j:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))