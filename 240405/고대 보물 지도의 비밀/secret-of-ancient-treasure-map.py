from sys import maxsize
from collections import deque

# 음수가 k개까지 허용되는 dp 테이블 초기화
def init_dp(n):
    dp = [-maxsize for _ in range(n + 1)]
    dp[0] = 0
    return dp

n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

# 부분 연속합을 dp[i]에 저장
    # 음수의 개수가 k개 초과일 때
        # 가장 빠른 순서의 음수까지의 부분 연속합을 빼고 새로운 음수를 추가한 값과  새로운 음수의 값 중 최대값을 dp[i]에 저장
        # 음수가 등장하는 순서는 deque로 관리
dp = init_dp(n)
q = deque()
cur_k = 0
for i in range(1, n + 1):
    # 추가되는 수가 음수 일 때
        # 큐에 음수가 추가되었을 때의 dp테이블 인덱스를 추가하고 현재 음수 개수를 1 증가
    if nums[i - 1] < 0:
        q.append(i)
        cur_k += 1

        # 현재 음수 개수가 k개 이하일 때
            # 직전 최대 부분 연속합과 음수의 합이 음수보다 작으면
                # dp[i]는 새로운 음수값
                # 큐는 비우고 새로운 음수가 추가된 때의 dp테이블 인덱스를 삽입
                # 현재 음수 개수는 1
            # 직전 최대 부분 연속합과 음수의 합이 음수보다 작지 않으면
                # dp[i]는 직전 최대 부분 연속합과 음수의 합
        if cur_k <= k:
            if dp[i - 1] + nums[i - 1] < nums[i - 1]:
                dp[i] = nums[i - 1]
                q.clear()
                q.append(i)
                cur_k = 1
            else:
                dp[i] = dp[i - 1] + nums[i - 1]

        # 현재 음수 개수가 k개 초과일 때
            # 가장 먼저 등장하는 음수까지의 최대 연속 부분합을 직전 연속 최대 부분합에서 뺀 값을 tmp로 사용
                # tmp에 새로운 음수를 더한 값과 새로운 음수 중 최대값을 dp[i]에 저장
        else:
            front_odd = q.popleft()
            tmp = dp[i - 1] - dp[front_odd]
            if tmp + nums[i - 1] < nums[i - 1]:
                dp[i] = nums[i - 1]
                q.clear()
                q.append(i)
                cur_k = 1
            else:
                dp[i] = tmp + nums[i - 1]
    else:
        dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])
print(max(dp))