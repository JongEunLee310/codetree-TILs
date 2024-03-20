n, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]

max_rec = -1
# 왼쪽 위 꼭지점이 (i, j)이고 오른쪽 아래 꼭지점이 (a, b)인 직사각형 중 최대 양수 직사각형을 탐색
for i in range(n):
    for j in range(m):
        for a in range(i, n):
            for b in range(j, m):
                rec = 0
                for c in range(i, a + 1):
                    sig = True
                    for d in range(j, b + 1):
                        if grid[c][d] <= 0:
                            rec = 0
                            sig = False
                            break
                        rec += 1
                    if not sig: break
                if rec > 0:
                    max_rec = max(max_rec, rec)

print(max_rec)