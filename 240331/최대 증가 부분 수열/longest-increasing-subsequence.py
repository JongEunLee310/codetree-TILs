N = int(input())
nums = [int(x) for x in input().split()]
dp = [1 for _ in range(N)]

for i in range(1, N):
    max_len = 0
    for j in range(i):
        if nums[j] < nums[i]:
            max_len = max(max_len, dp[j])
    dp[i] = max_len + 1
print(max(dp))