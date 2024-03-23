import heapq

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def move_marbles(n, m, t, l, count, marbles):
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    for _ in range(t):
        # 남아있는 구슬 이동
        for i in range(m):
            r, c, d, v, _ = marbles[i]
            for j in range(v):
                nr, nc = r + dy[d], c + dx[d]
                if not in_range(nr, nc, n, n):
                    d = (d + 2) % 4
                    marbles[i][2] = d
                    nr, nc = r + dy[d], c + dx[d]
                
                count[nr][nc] += 1
                count[r][c] -= 1
                marbles[i][0], marbles[i][1] = nr, nc
                r, c = nr, nc
                
        # 남아있는 구슬 이동 후 한 칸에 l개 이상 있는 구슬 제거
        for i in range(n):
            for j in range(n):
                if count[i][j] > l:
                    # 우선순위가 낮은 순으로 소멸 구슬 탐색
                    out_cnt = count[i][j] - l
                    out = []
                    for k in range(m):
                        if marbles[k][0] == i and marbles[k][1] == j:
                            # 힙을 사용해서 우선순위가 낮은 구슬만 힙에 저장
                            if len(out) < out_cnt:
                                heapq.heappush(out, [-marbles[k][3], -marbles[k][4], marbles[k]])
                            else:
                                # 우선순위가 낮은 경우거나 우선순위가 같지만 구슬의 숫자가 작은 경우 힙에 저장
                                if -out[0][0] > marbles[k][3] or -out[0][0] == marbles[k][3] and -out[0][1] > marbles[k][4]:
                                    heapq.heappop(out)
                                    heapq.heappush(out, [-marbles[k][3], -marbles[k][4], marbles[k]])
                    count[i][j] = l

                    # 힙에 저장된 구슬을 marbles 리스트에서 제거
                    for k in range(out_cnt):
                        marbles.remove(out[k][-1])
                        m -= 1

    return m

n, m, t, k = [int(x) for x in input().split()]
marbles = [input().split() for _ in range(m)]

# count 배열 초기화 및 입력으로 들어온 marbles 요소를 정수로 변환
dir_dict = {'U' : 0, 'D' : 2, 'R' : 1, 'L' : 3}
count = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    r, c, d, v = int(marbles[i][0]) - 1, int(marbles[i][1]) - 1, dir_dict[marbles[i][2]], int(marbles[i][3])
    marbles[i] = [r, c, d, v, i]
    count[r][c] += 1

exist_m = move_marbles(n, m, t, k, count, marbles)
print(exist_m)