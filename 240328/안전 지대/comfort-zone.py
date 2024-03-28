def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def dfs(n, m, h, v, k, dx, dy, x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny, m, n) and v[ny][nx] == 0 and h[ny][nx] > k:
            v[ny][nx] = 1
            dfs(n, m, h, v, k, dx, dy, nx, ny)

N, M = [int(x) for x in input().split()]
houses = [[int(x) for x in input().split()] for _ in range(N)]

# 집 중 가장 높은 집의 높이가 k의 상한선이다.
max_height = 0
for i in range(N):
    max_height = max(max_height, max(houses[i]))

# k보다 큰 숫자가 있는 곳부터 dfs로 방문하는 것을 방문하여 안전 영역의 개수를 구한다.
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
max_k, max_area = 1, 0
for k in range(1, max_height + 1):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    area = 0
    for i in range(N):
        for j in range(M):
            if houses[i][j] > k and visited[i][j] == 0:
                area += 1
                visited[i][j] = 1
                dfs(N, M, houses, visited, k, dx, dy, j, i)

    if area > max_area:
        max_k, max_area = k, area

print(max_k, max_area)