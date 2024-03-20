n, t = [int(x) for x in input().split()]
belt = [[int(x) for x in input().split()] for _ in range(2)]

for i in range(t):
    down, up = belt[0][-1], belt[1][-1]
    # 위쪽 벨트 이동
    for j in range(n - 1, 0, -1):
        belt[0][j] = belt[0][j - 1]
    belt[0][0] = up

    # 아래쪽 벨트 이동
    for j in range(n - 1, 0, -1):
        belt[1][j] = belt[1][j - 1]
    belt[1][0] = down

for i in range(2):
    for j in range(n):
        print(belt[i][j], end=' ')
    print()