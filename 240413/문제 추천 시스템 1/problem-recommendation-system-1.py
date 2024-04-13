from sortedcontainers import SortedSet

n = int(input())
problems = SortedSet([tuple([int(x) for x in input().split()][::-1]) for _ in range(n)])
m = int(input())
for _ in range(m):
    cmd = input().split()
    if cmd[0] == 'rc':
        if int(cmd[1]) == 1:
            print(problems[-1][1])
        elif int(cmd[1]) == -1:
            print(problems[0][1])
    elif cmd[0] == 'ad':
        problems.add((int(cmd[2]), int(cmd[1])))
    elif cmd[0] == 'sv':
        if (int(cmd[2]), int(cmd[1])) in problems:
            problems.remove((int(cmd[2]), int(cmd[1])))