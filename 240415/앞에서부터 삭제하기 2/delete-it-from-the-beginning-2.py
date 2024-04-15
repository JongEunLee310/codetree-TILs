import heapq

N = int(input())
pq = [int(x) for x in input().split()]

max_avg = 0
for K in range(1, N - 1):
    pq2 = pq[K:]
    heapq.heapify(pq2)
    heapq.heappop(pq2)
    max_avg = max(max_avg, sum(pq2) / len(pq2))
print("{0:.2f}".format(max_avg))