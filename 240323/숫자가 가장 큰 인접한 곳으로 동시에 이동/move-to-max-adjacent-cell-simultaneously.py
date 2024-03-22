def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

n, m, t = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]
marbles = [[int(x) - 1 for x in input().split()] for _ in range(m)]

# 격자 내 위치별 구슬 개수 정보를 가진 count 2차원 리스트 초기화
count = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    r, c = marbles[i][0], marbles[i][1]
    count[r][c] = 1

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
for _ in range(t):
    # 구슬 이동
    for i in range(m):
        # dx, dy의 인덱스를 상하좌우 순으로 생성하여 max_value가 같을 때 먼저 탐색한 위치가 최대 인접 위치로 확정
        max_value, max_x, max_y = 0, 0, 0
        for j in range(4):
            nx, ny = marbles[i][1] + dx[j], marbles[i][0] + dy[j]
            if in_range(nx, ny, n, n) and grid[ny][nx] > max_value:
                max_value = grid[ny][nx]
                max_x, max_y = nx, ny
            
            
        # count 2차원 리스트에서 이전 위치의 구슬 수를 1만큼 감소시키고 다음 위치의 구슬 수를 1만큼 증가 후 구슬의 위치 수정
        count[marbles[i][0]][marbles[i][1]] -= 1
        count[max_y][max_x] += 1
        marbles[i][0], marbles[i][1] = max_y, max_x

    # count 2차원 리스트에서 2이상의 값의 위치를 찾아 0으로 만들고 해당 위치에 있던 구슬을 marbles 리스트에서 제거
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0
                while True:
                    try:
                        marbles.remove([i, j])
                        m -= 1
                    except:
                        break

cnt = 0
for i in range(n):
    cnt += sum(count[i])
print(cnt)