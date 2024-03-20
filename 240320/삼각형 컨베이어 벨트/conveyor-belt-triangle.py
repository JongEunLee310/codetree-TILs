n, t = [int(x) for x in input().split()]
belt = [[int(x) for x in input().split()] for _ in range(3)]

for _ in range(t):
    b1, b2, b3 = belt[0][-1], belt[1][-1], belt[2][-1]
    for i in range(n - 1, 0, -1):
        belt[0][i] = belt[0][i - 1]
        belt[1][i] = belt[1][i - 1] 
        belt[2][i] = belt[2][i - 1]
    belt[0][0], belt[1][0], belt[2][0] = b3, b1, b2

for i in range(3):
    for j in range(n):
        print(belt[i][j], end=' ')
    print()