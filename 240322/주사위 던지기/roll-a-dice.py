def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

n, m, r, c = [int(x) for x in input().split()]
rolling = input().split()
grid = [[0 for _ in range(n)] for _ in range(n)]

dir_dict = {'L' : 0, 'R' : 1, 'U' : 2, 'D' : 3}
dice = [1, 2, 3]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
r, c = r - 1, c - 1
grid[r][c] = 7 - dice[0]
for i in range(m):
    nx, ny = c + dx[dir_dict[rolling[i]]], r + dy[dir_dict[rolling[i]]]
    if in_range(nx, ny, n, n):
        c, r = nx, ny
        tmp = []
        if rolling[i] == 'L':
            tmp.append(dice[2])
            tmp.append(dice[1])
            tmp.append(7 - dice[0])
            grid[r][c] = 7 - dice[2]
        elif rolling[i] == 'R':
            tmp.append(7 - dice[2])
            tmp.append(dice[1])
            tmp.append(dice[0])
            grid[r][c] = dice[2]
        elif rolling[i] == 'U':
            tmp.append(dice[1])
            tmp.append(7 - dice[0])
            tmp.append(dice[2])
            grid[r][c] = 7 - dice[1]
        elif rolling[i] == 'D':
            tmp.append(7 - dice[1])
            tmp.append(dice[0])
            tmp.append(dice[2])
            grid[r][c] = dice[1]
        dice = tmp

result = 0
for i in range(n):
    result += sum(grid[i])
print(result)