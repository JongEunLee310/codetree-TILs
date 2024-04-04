from sys import maxsize

n = int(input())
nums = [int(x) for x in input().split()]

# 전체 합이 짝수이면 두 그룹의 합이 같을 수 있음
total = sum(nums)
if total % 2 == 0:
    # 전체 합의 절반을 최소 하나의 값으로 만들 수 있다면 성공
        # 각 인덱스가 전체 합의 절반까지의 숫자들의 합을 의미
        # 인덱스의 값이 maxsize이면 합을 만들 수 없는 것이고 n과 같으면 두 그룹으로 나눌 수 없음을 의미
    half_total = total // 2
    dp = [maxsize for _ in range(half_total + 1)]
    dp[0] = 0
    for num in nums:
        for i in range(half_total, 0, -1):
            if i - num >= 0:
                dp[i] = min(dp[i], dp[i - num] + 1)
        
    print('Yes' if dp[-1] < maxsize or dp[-1] < n else 'No')
# 전체 합이 홀수이면 두 그룹으로 나누었을 때 합이 같을 수 없으므로 No를 출력 
else:
    print('No')