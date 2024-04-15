import heapq
from collections import deque

N = int(input())
# 숫자의 최소값을 빠르게 찾기 위해 pq를 사용
pq = [int(x) for x in input().split()]
# 앞에서부터 순서대로 숫자를 삭제하기 위해 deque로 숫자의 순서를 관리
nums = deque(pq)

heapq.heapify(pq)
max_avg = 0
for K in range(1, N - 1):
    # deque의 맨 앞에 있는 숫자를 pq에서 제거
    pq.remove(nums.popleft())

    # pq에서 가장 작은 수를 제외한 나머지 수의 평균을 구한 후 최대 평균과 비교 
    min_num = heapq.heappop(pq)
    max_avg = max(max_avg, sum(pq) / len(pq))

    # 제외한 최소값을 다시 pq에 넣어준다.
    heapq.heappush(pq, min_num)
print("{0:.2f}".format(max_avg))