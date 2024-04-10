from sortedcontainers import SortedDict

n = int(input())
s = SortedDict()
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'add':
        s[int(cmd[1])] = int(cmd[2])
    elif cmd[0] == 'remove':
        s.pop(int(cmd[1]))
    elif cmd[0] == 'find':
        print(s[int(cmd[1])] if int(cmd[1]) in s else None)
    elif cmd[0] == 'print_list':
        if len(s) == 0:
            print(None)
            continue
        for _, item in s.items():
            print(item, end=' ')
        print()