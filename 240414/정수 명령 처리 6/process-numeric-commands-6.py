import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        heapq.heappush(self.items, -item)
    
    def pop(self):
        if self.empty():
            raise Exception("PriorityQueue is empty.")

        return -heapq.heappop(self.items)

    def size(self):
        return len(self.items)
    
    def empty(self):
        return not self.items
    
    def top(self):
        if self.empty():
            raise Exception("PriorityQueue is empty.")
        
        return -self.items[0]

N = int(input())
pq = PriorityQueue()
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        pq.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(pq.pop())
    elif cmd[0] == 'size':
        print(pq.size())
    elif cmd[0] == 'empty':
        print(1 if pq.empty() else 0)
    elif cmd[0] == 'top':
        print(pq.top())