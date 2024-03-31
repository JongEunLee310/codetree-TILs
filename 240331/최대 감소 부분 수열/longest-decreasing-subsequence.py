N = int(input())
nums = [int(x) for x in input().split()]
dp = [1 for _ in range(N)]

# 현재 검사하는 인덱스의 값보다 작은 값 중 최대 길이에 1을 더한 값을 dp[i]에 저장
for i in range(1, N):
    max_len = 0
    for j in range(i):
        if nums[j] > nums[i]:
            max_len = max(max_len, dp[j])
    dp[i] = max_len + 1
print(max(dp))