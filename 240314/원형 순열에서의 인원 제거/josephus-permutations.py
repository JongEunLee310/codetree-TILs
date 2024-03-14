from collections import deque

q = deque()
N, K = [int(x) for x in input().split()]
for i in range(1, N + 1):
    q.append(i)

while len(q) > 0:
    for _ in range(K - 1):
        q.append(q.popleft())
    print(q.popleft(), end=' ')