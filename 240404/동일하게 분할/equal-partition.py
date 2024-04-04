from sys import maxsize

n = int(input())
nums = [int(x) for x in input().split()]

total = sum(nums)
if total % 2 == 0:
    half_total = total // 2
    dp = [maxsize for _ in range(half_total + 1)]
    dp[0] = 0
    for num in nums:
        for i in range(half_total, 0, -1):
            if i - num >= 0:
                dp[i] = min(dp[i], dp[i - num] + 1)
        
    print('Yes' if dp[-1] < maxsize else 'No')
else:
    print('No')