def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

N = int(input())
x, y = [int(x) - 1 for x in input().split()]
miro = [input() for _ in range(N)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
Dir, t, turn_cnt = 0, 0, 0  # turn_cnt는 제자리에서 반시계 방향으로 회전하는 횟수, 4이상이면 탈출 불가능으로 판단
sx, sy, sDir = x, y, Dir
while True:
    # 출발할 때 방향으로 출발 지점으로 되돌아오거나 제자리에서 회전만 한다면 탈출 불가능
    if x == sx and y == sy and Dir == sDir and t > 0 or turn_cnt >= 4:
        t = -1
        break

    nx, ny = x + dx[Dir], y + dy[Dir]
    # 진행 방향으로 다음 칸이 격자 밖이면 탈출
    if not in_range(nx, ny, N, N):
        x, y = nx, ny
        t += 1
        break
    else:
        # 진행 방향으로 다음 칸이 벽이면 반시계 방향으로 90도 회전
        if miro[nx][ny] == '#':
            Dir = (Dir + 3) % 4
            turn_cnt += 1
        # 진행 방향으로 다음 칸이 비어 있을 때 오른쪽이 벽이면 그대로 진행, 아니면 시계방향으로 90도 회전 후 한 칸 더 전진
        elif miro[nx][ny] == '.':
            if miro[nx + dx[(Dir + 1) % 4]][ny + dy[(Dir + 1) % 4]] == '#':
                x, y = nx, ny
            else:
                Dir = (Dir + 1) % 4
                x, y = nx + dx[Dir], ny + dy[Dir]
                t += 1
            t += 1
            turn_cnt = 0    # 이동했다면 제자리에서 회전하는 것이 아니므로 turn_cnt를 0으로 초기화

print(t)