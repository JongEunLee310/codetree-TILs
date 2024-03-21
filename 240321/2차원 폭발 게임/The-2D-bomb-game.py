def explode(bombs, M):
    # sig가 True일 때 while 실행
    sig = True
    explode = []
    while len(bombs) > 0 and sig:
        explode = []
        sig = False

        # M개 이상 같은 숫자인 폭탄 구간 탐색
        cur = bombs[0]
        cnt = 0
        for i in range(len(bombs)):
            if bombs[i] == cur:
                cnt += 1
            else:
                if cnt >= M:
                    explode.append([i - cnt, i - 1])
                    sig = True
                cur = bombs[i]
                cnt = 1
        # for 문 이후 추가되지 못한 M개 이상 같은 숫자 폭탄 구간 추가    
        if cnt >= M:
            explode.append([len(bombs) - cnt, len(bombs) - 1])
            sig = True

        if sig:
            # 폭발 구간을 0으로 변경
            for i in range(len(explode)):
                for j in range(len(bombs)):
                    if j >= explode[i][0] and j <= explode[i][1]:
                        bombs[j] = 0
            # 중력 작용 적용
            new_bombs = []
            for i in range(len(bombs)):
                if bombs[i] != 0:
                    new_bombs.append(bombs[i])
            
            bombs = new_bombs

    return bombs

def rotate_90(grid):
    new_grid = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    # 90도 시계방향으로 회전한 것을 new_grid에 적용
    for i in range(len(grid)):
        for j in range(len(grid)):
            new_grid[j][i] = grid[-1 - i][j]

    # 중력 작용 적용 new_grid -> grid로 옮김
    for i in range(len(new_grid)):
        tmp = []
        for j in range(len(new_grid)):
            if new_grid[j][i] != 0:
                tmp.append(new_grid[j][i])

        for j in range(-1, -len(grid) - 1, -1):
            try:
                grid[j][i] = tmp[j]
            except:
                grid[j][i] = 0

N, M, K = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(N)]

for k in range(K):
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(grid[j][i])
        tmp = explode(tmp, M)

        for j in range(-1, -N - 1, -1):
            try:
                grid[j][i] = tmp[j]
            except:
                grid[j][i] = 0
    
    rotate_90(grid)

cnt = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            cnt += 1
print(cnt)