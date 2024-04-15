import heapq

N = int(input())
nums = [int(x) for x in input().split()]

# 숫자를 nums에 입력된 순서에 거꾸로 pq에 추가하며 최대 평균값을 계산
pq = [nums[-1]]
total, max_avg = nums[-1], nums[-1]
for i in range(N - 2, 1, -1):
    heapq.heappush(pq, nums[i])
    total += nums[i]

    # 남은 수 중 최소값을 제외한 평균과 이전 최대 평균값을 비교해 최대 평균값을 구한다.
    min_num = heapq.heappop(pq)
    total -= min_num
    max_avg = max(max_avg, total / len(pq))

    # 최소값을 다시 pq에 복원
    heapq.heappush(pq, min_num)
    total += min_num

print("{0:.2f}".format(max_avg))