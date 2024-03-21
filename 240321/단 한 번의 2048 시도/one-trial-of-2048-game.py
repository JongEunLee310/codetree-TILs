def move_right(g):
    for i in range(4):
        # 공백을 매움
        tmp = []
        for j in range(4):
            if g[i][j] != 0:
                tmp.append(g[i][j])
        
        # 같은 숫자 합성 후 추가 이동
        EoT = 0 # End of Tmp
        for j in range(len(tmp) - 1, 0, -1):
            if tmp[j] != 0 and tmp[j] == tmp[j - 1]:
                tmp[j] *= 2
                for k in range(j - 1, EoT, -1):
                    tmp[k] = tmp[k - 1]
                tmp[EoT] = 0
                EoT += 1
        
        # tmp를 원래 격자에 적용
        for j in range(-1, -5, -1):
            try:
                g[i][j] = tmp[j]
            except:
                g[i][j] = 0

def move_left(g):
    for i in range(4):
        # 공백을 매움
        tmp = []
        for j in range(4):
            if g[i][j] != 0:
                tmp.append(g[i][j])
        
        # 같은 숫자 합성 후 추가 이동
        EoT = len(tmp) - 1 # End of Tmp
        for j in range(len(tmp) - 1):
            if tmp[j] != 0 and tmp[j] == tmp[j + 1]:
                tmp[j] *= 2
                for k in range(j + 1, EoT):
                    tmp[k] = tmp[k + 1]
                tmp[EoT] = 0
                EoT -= 1
        
        # tmp를 원래 격자에 적용
        for j in range(4):
            try:
                g[i][j] = tmp[j]
            except:
                g[i][j] = 0

def move_up(g):
    for i in range(4):
        # 공백을 매움
        tmp = []
        for j in range(4):
            if g[j][i] != 0:
                tmp.append(g[j][i])
        
        # 같은 숫자 합성 후 추가 이동
        EoT = len(tmp) - 1 # End of Tmp
        for j in range(len(tmp) - 1):
            if tmp[j] != 0 and tmp[j] == tmp[j + 1]:
                tmp[j] *= 2
                for k in range(j + 1, EoT):
                    tmp[k] = tmp[k + 1]
                tmp[EoT] = 0
                EoT -= 1
        
        # tmp를 원래 격자에 적용
        for j in range(4):
            try:
                g[j][i] = tmp[j]
            except:
                g[j][i] = 0

def move_down(g):
    for i in range(4):
        # 공백을 매움
        tmp = []
        for j in range(4):
            if g[j][i] != 0:
                tmp.append(g[j][i])
        
        # 같은 숫자 합성 후 추가 이동
        EoT = 0 # End of Tmp
        for j in range(len(tmp) - 1, 0, -1):
            if tmp[j] != 0 and tmp[j] == tmp[j - 1]:
                tmp[j] *= 2
                for k in range(j - 1, EoT, -1):
                    tmp[k] = tmp[k - 1]
                tmp[EoT] = 0
                EoT += 1
        
        # tmp를 원래 격자에 적용
        for j in range(-1, -5, -1):
            try:
                g[j][i] = tmp[j]
            except:
                g[j][i] = 0

grid = [[int(x) for x in input().split()] for _ in range(4)]
direction = input()

# 방향에 따라 다른 함수를 사용
if direction == 'L':
    move_left(grid)
elif direction == 'R':
    move_right(grid)
elif direction == 'U':
    move_up(grid)
elif direction == 'D':
    move_down(grid)

for i in range(4):
    for j in range(4):
        print(grid[i][j], end=' ')
    print()