from sys import maxsize

# 숫자와 시작점, 도착점의 위치를 찾는 함수
def get_loc(g):
    num_loc = {}
    e, s = [], []
    max_n = 0
    for i in range(len(g)):
        for j in range(len(g)):
            cur = g[i][j]
            if cur == 'E': e = [i, j]
            elif cur == 'S': s = [i, j]
            elif cur.isnumeric():
                max_n = max(max_n, int(cur))
                num_loc[int(cur)] = [i, j]
    
    new_num_loc = [s]
    for i in range(1, max_n + 1):
        if i in num_loc:
            new_num_loc.append(num_loc[i])
            i += 1
    
    return new_num_loc, e

# 숫자를 3개 선택해서 최소로 움직인 거리를 구하는 함수
def min_move(num_loc, e, cur, cnt, path):
    if len(num_loc) <= 3: return -1
    if cnt >= 3: return get_dist(num_loc, e, path)
    if cur >= len(num_loc):
        if cnt >= 3: return get_dist(num_loc, e, path)
        else: return maxsize

    min_m, d1 = maxsize, maxsize
    # 현재 위치를 포함한 경로의 거리
    if cur > 0: # 출발점은 이미 경로에 포함되어 있으므로 다시 추가하지 않아도 됨
        path.append(cur)
        d1 = min_move(num_loc, e, cur + 1, cnt + 1, path)
        path.pop()

    # 현재 위치를 제외한 경로의 거리
    d2 = min_move(num_loc, e, cur + 1, cnt, path)

    min_m = min(min_m, d1, d2)

    return min_m

# 경로상 거리를 구하는 함수
def get_dist(num_loc, e, path):
    dist = 0
    for i in range(1, len(path)):
        dist += abs(num_loc[path[i]][0] - num_loc[path[i - 1]][0]) + abs(num_loc[path[i]][1] - num_loc[path[i - 1]][1])
    dist += abs(e[0] - num_loc[path[-1]][0]) + abs(e[1] - num_loc[path[-1]][1])
    return dist

n = int(input())
grid = [input() for _ in range(n)]
# 숫자와 시작점, 도착점 위치 초기화
num_loc, e = get_loc(grid)
print(min_move(num_loc, e, 0, 0, [0]))