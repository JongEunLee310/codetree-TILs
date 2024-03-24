def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

# 최대 폭발 영역을 구하는 함수 - g: grid, n: 폭발 위치 개수, loc : 폭발 위치, b : 종류별 폭발 영역
def get_maximum_area(g, n, loc, b):
    # 폭탄이 모두 배치되었으면 폭발 영역 개수 반환
    if n == len(loc):
        return get_area(g,loc, b)

    max_area = 0
    r, c = loc[n]
    for i in range(1, 4):
        grid[r][c] = i
        max_area = max(max_area, get_maximum_area(g, n + 1, loc, b))

    return max_area

# 폭발 영역을 구하는 함수
def get_area(g, loc, b):
    # 새로운 격자에 폭발 영역 표시
    new_grid = [[0 for _ in range(len(g))] for _ in range(len(g))]
    for r, c in loc:
        new_grid[r][c] = -1
        for i in range(4):
            tr, tc = r + b[grid[r][c]][i][0], c + b[grid[r][c]][i][1]
            if in_range(tr, tc, len(g), len(g)):
                new_grid[tr][tc] = -1

    # 폭발 영역의 개수 카운트
    result = 0
    for i in range(len(g)):
        result += -sum(new_grid[i])
    
    return result

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]

# 폭탄의 위치 만을 탐색하기 위해 폭탄 위치 초기화
bomb_loc = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1: bomb_loc.append([i, j])

# 폭탄 종류별 폭발 영역을 미리 설정
bombs = {1 : [[-2, 0], [-1, 0], [1, 0], [2, 0]], 2 : [[-1, 0], [0, 1], [1, 0], [0, -1]], 3 : [[-1, -1], [-1, 1], [1, 1], [1, -1]]}

print(get_maximum_area(grid, 0, bomb_loc, bombs))