def move_right(M, r, building):
    tmp = building[r][-1]
    for i in range(M - 1, 0, -1):
        building[r][i] = building[r][i - 1]
    building[r][0] = tmp

def move_left(M, r, building):
    tmp = building[r][0]
    for i in range(M - 1):
        building[r][i] = building[r][i + 1]
    building[r][-1] = tmp

def to_top_check(l, M, building):
    result = False
    for i in range(M):
        if building[l + 1][i] == building[l][i]:
            result = True
            break
    return result

def to_bottom_check(l, M, building):
    result = False
    for i in range(M):
        if building[l - 1][i] == building[l][i]:
            result = True
            break
    return result

N, M, Q = [int(x) for x in input().split()]
building = [[int(x) for x in input().split()] for _ in range(N)]
w_info = [input().split() for _ in range(Q)]

for i in range(Q):
    r, d = w_info[i]
    r = int(r) - 1

    # 바람이 분 행 이동
    move_right(M, r, building) if d == 'L' else move_left(M, r, building)

    # 영향 전파
    to_top, to_bottom = r - 1, r + 1
    while to_top >= 0 or to_bottom < N:
        d = 'R' if d =='L' else 'L'

        if to_top >= 0 and to_top_check(to_top, M, building):
            move_right(M, to_top, building) if d == 'L' else move_left(M, to_top, building)
            to_top -= 1
        else: to_top = -1
        
        if to_bottom < N and to_bottom_check(to_bottom, M, building):
            move_right(M, to_bottom, building) if d == 'L' else move_left(M, to_bottom, building)
            to_bottom += 1
        else: to_bottom = N

for i in range(N):
    for j in range(M):
        print(building[i][j], end=' ')
    print()