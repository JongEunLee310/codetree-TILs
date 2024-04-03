def get_pre_increase(n, nums):
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def get_pre_decrease(n, nums):
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def get_post_increase(n, nums):
    dp = [1 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def get_post_decrease(n, nums):
    dp = [1 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

N = int(input())
nums = [int(x) for x in input().split()]

# 해당 위치의 숫자 이전에 증가하는 경우와 감소하는 경우 중 가장 긴 구간의 개수를 초기화
pre_in_dp = get_pre_increase(N, nums)
pre_de_dp = get_pre_decrease(N, nums)

# 해당 위치의 숫자 이후에 증가하는 경우와 감소하는 경우 중 가장 긴 구간의 개수를 초기화
post_in_dp = get_post_increase(N, nums)
post_de_dp = get_post_decrease(N, nums)

# 현재 위치를 기준으로 이전 증가 + 이후 감소, 이전 증가 + 이후 증가, 이전 감소 + 이후 감소 인 것 중 최대를 찾는다.
max_len = 0
for i in range(N):
    l1 = pre_in_dp[i] + post_de_dp[i] - 1
    l2 = pre_in_dp[i] + post_in_dp[i] - 1
    l3 = pre_de_dp[i] + post_de_dp[i] - 1
    max_len = max(max_len, l1, l2, l3)
print(max_len)