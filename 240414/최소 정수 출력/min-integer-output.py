import heapq

n = int(input())
pq = []
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        if len(pq) == 0:
            print(0)
        else:
            print(pq[0])
            heapq.heappop(pq)
    else:
        heapq.heappush(pq, cmd)