n, m, k = [int(x) for x in input().split()]
grid = [' ' * (m + 1)] + [' ' + input() for _ in range(n)]

# 알파벳 a, b, c에 대한 각각의 누적합 테이블을 초기화
prefix_sum = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(3)]
for i in range(3):
    cur = chr(ord('a') + i)
    for j in range(1, n + 1):
        for l in range(1, m + 1):
            # 이전까지 고려한 누적합의 합에서 중복을 제거
            prefix_sum[i][j][l] = prefix_sum[i][j - 1][l] + prefix_sum[i][j][l - 1] - prefix_sum[i][j - 1][l - 1]
            # 현재 검사 중인 격자칸의 알파벳이 cur과 같을 때 현재까지 누적합에 1 추가
            if grid[j][l] == cur:
                prefix_sum[i][j][l] += 1

# 누적합 좌표 (r2, c2)의 값 - (r1 - 1, c2)의 값 - (r2, c1 - 1)값 + (r1 - 1, c1 - 1)의 값이 정답
for _ in range(k):
    r1, c1, r2, c2 = [int(x) for x in input().split()]
    for i in range(3):
        ans = prefix_sum[i][r2][c2] - prefix_sum[i][r1 - 1][c2] - prefix_sum[i][r2][c1 - 1] + prefix_sum[i][r1 - 1][c1 - 1]
        print(ans, end=' ')
    print()