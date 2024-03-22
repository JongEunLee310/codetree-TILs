from collections import deque

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

N, M, K = [int(x) for x in input().split()]
apple = [[int(x) - 1 for x in input().split()] for _ in range(M)]
snake_move = [input().split() for _ in range(K)]
grid = [[0 for _ in range(N)] for _ in range(N)]

# 격자에 사과 위치와 뱀 위치 초기화 - 사과 : 1, 뱀 : 2
grid[0][0] = 2
for i in range(M):
    y, x = apple[i]
    grid[y][x] = 1

# 뱀의 머리, 몸통, 꼬리의 위치는 큐로 관리
snake = deque()
snake.append([0, 0])

# 뱀 이동
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
dir_dict = {'R' : 0, 'D' : 1, 'L' : 2, 'U' : 3}
t = 0
for i in range(K):
    sig = True
    Dir, dist = dir_dict[snake_move[i][0]], int(snake_move[i][1])
    for j in range(dist):
        nx, ny = snake[-1][1] + dx[Dir], snake[-1][0] + dy[Dir]
        if not in_range(nx, ny, N, N):
            sig = False
            t += 1
            break
        else:
            # 다음 칸이 뱀일 때
            if grid[ny][nx] == 2:
                # 다음 칸이 뱀의 꼬리 일 때는 꼬리를 지우고 머리 이동
                if ny == snake[0][0] and nx == snake[0][1]:
                    snake.append(snake.popleft())
                    t += 1
                # 다음 칸이 뱀의 꼬리가 아닐 때 정지
                else:
                    sig = False
                    t += 1
                    break
            # 다음 칸이 뱀일 때 뱀 길이 추가
            elif grid[ny][nx] == 1:
                grid[ny][nx] = 2
                snake.append([ny, nx])
                t += 1
            # 다음 칸이 아무 것도 아닐 때 그냥 이동
            elif grid[ny][nx] == 0:
                tail = snake.popleft()
                grid[tail[0]][tail[1]] = 0
                grid[ny][nx] = 2
                snake.append([ny, nx])
                t += 1

    if not sig: break

print(t)