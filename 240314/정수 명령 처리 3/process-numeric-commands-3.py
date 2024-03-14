from collections import deque

dq = deque()
N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push_front': dq.append(int(cmd[1]))
    elif cmd[0] == 'push_back': dq.appendleft(int(cmd[1]))
    elif cmd[0] == 'pop_front': print(dq.pop())
    elif cmd[0] == 'pop_back': print(dq.popleft())
    elif cmd[0] == 'size': print(len(dq))
    elif cmd[0] == 'empty': print(0) if dq else print(1)
    elif cmd[0] == 'front': print(dq[-1])
    elif cmd[0] == 'back': print(dq[0])