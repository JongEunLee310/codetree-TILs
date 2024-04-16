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

cur = Node(input())
N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == '1':
        singleton = Node(cmd[1])
        insert_prev(cur, singleton)
    elif cmd[0] == '2':
        singleton = Node(cmd[1])
        insert_next(cur, singleton)
    elif cmd[0] == '3':
        if cur.prev != None:
            cur = cur.prev
    elif cmd[0] == '4':
        if cur.next != None:
            cur = cur.next

    print(cur.prev.data if cur.prev != None else '(Null)', end=' ')
    print(cur.data, end=' ')
    print(cur.next.data if cur.next != None else '(Null)', end=' ')
    print()