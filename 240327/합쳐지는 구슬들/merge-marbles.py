def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

# 구슬 정보를 가지고 있는 marbles 리스트의 값을 모두 정수형으로 변환하고 count 리스트 초기화하는 함수
def init_marbles(n, m, dx, dy):
    dir_dict = {'U' : 0, 'R' : 1, 'D' : 2, 'L' : 3}
    count = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(m)):
        m[i] = [int(m[i][0]) - 1, int(m[i][1]) - 1, dir_dict[m[i][2]], int(m[i][3])]
        count[m[i][0]][m[i][1]] = 1
    
    return m, count

# 1초 동안 구슬의 위치 변화를 구하는 함수
def move_marbles(n, marbles, count, dx, dy):
    # 모든 구슬을 각자의 방향으로 한 칸씩 이동하거나 이동할 수 없을 시 방향을 전환
    for i in range(len(marbles)):
        # i 인덱스에 구슬이 없을 때 다음 차례로 넘김
        if not marbles[i]: continue

        # i 인덱스에 구슬이 있을 때 구슬 이동
        r, c, d, w = marbles[i]
        nr, nc = r + dy[d], c + dx[d]
        if not in_range(nr, nc, n, n): marbles[i][2] = (d + 2) % 4
        else:
            count[r][c] -= 1
            count[nr][nc] += 1
            marbles[i][0], marbles[i][1] = nr, nc

    # 하나의 격자 칸에 2개 이상의 구슬이 있을 때 가장 번호가 큰 구슬을 제외하고 False로 변환, 살아남은 구슬의 무게는 함께 있던 구슬의 무게 합으로 변환
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                # 격자 내 위치가 [i, j]에서 충돌한 구슬을 탐색
                c_m = []
                for k in range(len(marbles)):
                    if marbles[k] and marbles[k][0] == i and marbles[k][1] == j:
                        c_m.append(k)
                
                # 가장 큰 번호의 구슬에 무게를 합치고 나머지 구슬은 제거
                for k in range(len(c_m) - 2, -1, -1):
                    marbles[c_m[-1]][3] += marbles[c_m[k]][3]
                    marbles[c_m[k]] = False
                
                count[i][j] = 1

n, m, t = [int(x) for x in input().split()]
marbles = [input().split() for _ in range(m)]

# 구슬 정보를 가지고 있는 marbles 리스트의 값을 모두 정수형으로 변환하고 count 리스트 초기화
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
marbles, count = init_marbles(n, marbles, dx, dy)

# t초 동안 구슬을 이동
for _ in range(t):
    move_marbles(n, marbles, count, dx, dy)

# 남은 구슬과 최대 무게 구슬 출력
cnt, max_weight = 0, 0
for i in range(len(marbles)):
    if marbles[i]:
        cnt += 1
        max_weight = max(max_weight, marbles[i][3])
print(cnt, max_weight)