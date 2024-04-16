class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert_next(u, singleton):
    singleton.prev = u
    singleton.next = u.next

    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

def insert_prev(u, singleton):
    singleton.prev = u.prev
    singleton.next = u

    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

def pop(u):
    if u.prev is not None:
        u.prev.next = u.next
    if u.next is not None:
        u.next.prev = u.prev

        u.prev = u.next = None

N = int(input())
Q = int(input())
nodes = {i : Node(i) for i in range(1, N + 1)}
for _ in range(Q):
    cmd = [int(x) for x in input().split()]
    if cmd[0] == 1:
        pop(nodes[cmd[1]])
    elif cmd[0] == 2:
        insert_prev(nodes[cmd[1]], nodes[cmd[2]])
    elif cmd[0] == 3:
        insert_next(nodes[cmd[1]], nodes[cmd[2]])
    elif cmd[0] == 4:
        print(nodes[cmd[1]].prev.data if nodes[cmd[1]].prev != None else 0, end=' ')
        print(nodes[cmd[1]].next.data if nodes[cmd[1]].next != None else 0, end=' ')
        print()


for i in range(1, N + 1):
    print(nodes[i].next.data if nodes[i].next != None else 0, end=' ')