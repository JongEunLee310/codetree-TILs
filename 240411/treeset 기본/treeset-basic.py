from sortedcontainers import SortedSet

n = int(input())
s = SortedSet()
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'add':
        s.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    elif cmd[0] == 'find':
        print('true' if int(cmd[1]) in s else 'false')
    elif cmd[0] == 'lower_bound':
        lower_bound = s.bisect_left(int(cmd[1]))
        print(s[lower_bound]) if lower_bound != None and lower_bound < len(s) else print(None)
    elif cmd[0] == 'upper_bound':
        upper_bound = s.bisect_right(int(cmd[1]))
        print(s[upper_bound] if upper_bound != None else None)
    elif cmd[0] == 'largest':
        try:
            print(s[-1])
        except:
            print(None)
    elif cmd[0] == 'smallest':
        print(s[0] if len(s) > 0 else None)