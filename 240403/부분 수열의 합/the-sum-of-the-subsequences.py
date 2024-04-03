from sys import maxsize

n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

# dp 테이블을 maxsize로 초기화하여 -maxsize이면 아직 검토 전임을 명시, nums의 숫자를 기준으로 현재 검사 중인 합을 만들 수 있는지 판단하며 만들 수 있다면 필요한 숫자의 개수를 dp[i]에 저장
dp = [maxsize for _ in range(m + 1)]
dp[0] = 0
for num in nums:
    for i in range(m, -1, -1):
        if i - num >= 0 and dp[i - num] != maxsize:
            dp[i] = min(dp[i], dp[i - num] + 1)

print('Yes' if dp[m] < maxsize else 'No')