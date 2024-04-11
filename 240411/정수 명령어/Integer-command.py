from sortedcontainers import SortedSet

T = int(input())
for _ in range(T):
    k = int(input())
    s = SortedSet()
    for _ in range(k):
        cmd = input().split()
        if cmd[0] == 'I':
            s.add(int(cmd[1]))
        elif cmd[0] == 'D':
            if cmd[1] == '1' and len(s) > 0:
                s.remove(s[-1])
            elif cmd[1] == '-1' and len(s) > 0:
                s.remove(s[0])
    
    if len(s) == 0:
        print('EMPTY')
    else:
        print(s[-1], s[0])