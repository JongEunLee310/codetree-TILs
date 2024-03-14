import heapq

n = int(input())
arr = [int(x) for x in input().split()]

heap = []
for i in range(n):
    heapq.heappush(heap, arr[i])

for i in range(n):
    print(heapq.heappop(heap), end=" ")