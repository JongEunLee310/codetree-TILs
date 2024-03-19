from sys import maxsize

def not_in_first_rec_range(x, y, a, b, c, d):
    return not (a <= x <= c and b <= y <= d)


n, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]

# 첫번째 직사각형의 위치를 뺀 나머지 부분의 최대값을 더한 두 직사각형의 합을 구한다.
max_sum = -maxsize
for i in range(n):
    for j in range(m):
        # 왼쪽 위 꼭지점의 좌표가 (i, j)인 첫번째 직사각형의 모든 형태를 탐색
        for a in range(i, n):
            for b in range(j, m):
                # 첫번째 직사각형의 합
                rec1_sum = 0
                for k in range(i, a + 1):
                    for l in range(j, b + 1):
                        rec1_sum += grid[k][l]
                
                # 두번째 직사각형에 포함된 수의 최대합
                max_rec2_sum = -maxsize
                for c in range(n):
                    for d in range(m):
                        if not not_in_first_rec_range(c, d, i, j, a, b):
                            continue
                        # 왼쪽 위 꼭지점의 좌표가 (i, j)이면서 첫번째 직사각형과 겹치지 않는 두번째 직사각형의 모든 형태를 탐색
                        for e in range(c, n):
                            for f in range(d, m):
                                if not not_in_first_rec_range(e, f, i, j, a, b):
                                    continue
                                rec2_sum = 0
                                for g in range(c, e + 1):
                                    sig = True
                                    for h in range(d, f + 1):
                                        if not not_in_first_rec_range(g, h, i, j, a, b):
                                            rec2_sum = -maxsize
                                            sig = False
                                            break
                                        rec2_sum += grid[g][h]
                                    if not sig: break
                                max_rec2_sum = max(max_rec2_sum, rec2_sum)
                max_sum = max(max_sum, rec1_sum + max_rec2_sum)

print(max_sum)