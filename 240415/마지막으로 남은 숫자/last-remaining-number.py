import heapq

n = int(input())
pq = [-int(x) for x in input().split()]
heapq.heapify(pq)

while len(pq) >= 2:
    n1 = heapq.heappop(pq)
    n2 = heapq.heappop(pq)

    diff = abs(n1 - n2)
    if diff == 0:
        continue
    heapq.heappush(pq, -diff)

print(-pq[0] if len(pq) > 0 else -1)