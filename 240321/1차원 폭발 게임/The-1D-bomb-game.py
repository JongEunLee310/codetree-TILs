N, M = [int(x) for x in input().split()]
bombs = [int(input()) for _ in range(N)]

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

print(len(bombs))
for i in range(len(bombs)):
    print(bombs[i])