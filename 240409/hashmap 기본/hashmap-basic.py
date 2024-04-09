n = int(input())
d = {}
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'add':
        d[int(cmd[1])] = int(cmd[2])
    elif cmd[0] == 'remove':
        d.pop(int(cmd[1]))
    elif cmd[0] == 'find':
        if int(cmd[1]) in d:
            print(d[int(cmd[1])])
        else:
            print(None)