import heapq

n = int(input())
nums = [int(x) for x in input().split()]
pq = []
for num in nums:
    heapq.heappush(pq, num)
    if len(pq) < 3:
        print(-1)
        continue
    
    result = 1
    min_three = []
    for _ in range(3):
        min_three.append(heapq.heappop(pq))
        result *= min_three[-1]
    
    print(result)
    for _ in range(3):
        heapq.heappush(pq, min_three.pop())