N = int(input())
arr = []
for i in range(N):
    cmd = input().split()

    if cmd[0] == 'push_back':
        arr.append(int(cmd[1]))
    elif cmd[0] == 'pop_back':
        arr.pop()
    elif cmd[0] == 'size':
        print(len(arr))
    elif cmd[0] == 'get':
        print(arr[int(cmd[1]) - 1])