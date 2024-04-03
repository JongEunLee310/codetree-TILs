n = int(input())
nums = [1, 2, 5]

# 현재 숫자를 만들 수 있는 1, 2, 5만큼 이전의 합의 방법의 수를 모두 더한 것을 dp[i]의 값으로 사용
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for num in nums:
        if i - num > 0:
            dp[i] += dp[i - num]
        elif i - num == 0:
            dp[i] += 1

print(dp[n] % 10007)