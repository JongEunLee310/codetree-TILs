import heapq

n, m = [int(x) for x in input().split()]
dots = [[int(x) for x in input().split()] for _ in range(n)]
pq = []
for x, y in dots:
    heapq.heappush(pq, [x + y, x, y])

for _ in range(m):
    dist, x, y = heapq.heappop(pq)
    heapq.heappush(pq, [dist + 4, x + 2, y + 2])
print(pq[0][1], pq[0][2])