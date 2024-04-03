from sys import maxsize

n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

# 중복을 없애기 위해 동전의 합을 구하는 dp와 반대로 수의 합이 기준이 아닌 숫자의 종류를 기준으로 반복문을 실행
dp = [maxsize for _ in range(m + 1)]
dp[0] = 0
for num in nums:
    for i in range(m, 0, -1):
        if i - num >= 0 and dp[i - num] < maxsize:
            dp[i] = min(dp[i], dp[i - num] + 1)

print(dp[-1] if dp[-1] < maxsize else -1)