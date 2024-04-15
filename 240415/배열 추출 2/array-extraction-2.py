import heapq

n = int(input())
pq = []
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        if len(pq) == 0:
            print(0)
        else:
            _, num = heapq.heappop(pq)
            print(num)
    else:
        heapq.heappush(pq, tuple([abs(cmd), cmd]))