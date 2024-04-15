import heapq

n = int(input())
pq = []
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        print(0) if len(pq) == 0 else print(-heapq.heappop(pq))
    elif cmd > 0:
        heapq.heappush(pq, -cmd)