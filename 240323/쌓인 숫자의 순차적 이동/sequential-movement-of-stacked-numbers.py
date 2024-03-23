def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

n, m = [int(x) for x in input().split()]
# 격자 내 숫자 이동을 리스트로 관리하기 위해 grid 초기화, 숫자들의 위치를 dict로 관리하기 위해 dict 초기화
grid = [[[] for _ in range(n)] for _ in range(n)]
num_loc = {}
for i in range(n):
    nums = [int(x) for x in input().split()]
    for j in range(n):
        grid[i][j].append(nums[j])
        num_loc[nums[j]] = [i, j, 0]
nums = [int(x) for x in input().split()]

# 숫자 이동
dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]
for N in nums:
    r, c, idx = num_loc[N]  # r, c는 격자 내 숫자의 위치, idx는 특정 격자 칸의 리스트에서 숫자가 위치한 인덱스
    max_value = 0
    # 인접한 8방향의 숫자 중 최대값의 위치 탐색
    for i in range(8):
        nr, nc = r + dy[i], c + dx[i]
        if in_range(nr, nc, n, n) and len(grid[nr][nc]) > 0:
            # 한 격자 칸에 여러 숫자가 있을 수 있으므로 격자 칸 전체 탐색
            for n1 in grid[nr][nc]:
                max_value = max(max_value, n1)
    # 옮겨갈 숫자의 위치가 없다면 옮기지 않는다.
    if max_value == 0:
        continue
    max_r, max_c = num_loc[max_value][0], num_loc[max_value][1]

    # 최대값의 위치로 숫자 이동
    # tmp를 사용해서 필요한 만큼의 숫자만 이동
    tmp = []
    for _ in range(len(grid[r][c]) - num_loc[N][2]):    # 옮길 숫자와 해당 숫자의 위에 있는 숫자를 옮기기 위해 (격자 칸 리스트의 길이 - 옮길 숫자의 격자 내 인덱스) 값 만큼 숫자를 옮겨 준다.
        tmp.append(grid[r][c].pop())
    for i in range(len(tmp)):
        new_num = tmp.pop()
        num_loc[new_num] = [max_r, max_c, len(grid[max_r][max_c])]
        grid[max_r][max_c].append(new_num)

for i in range(n):
    for j in range(n):
        if len(grid[i][j]) == 0: print(None, end=' ')
        else:
            for k in range(len(grid[i][j]) - 1, -1, -1):
                print(grid[i][j][k], end=' ')
        print()