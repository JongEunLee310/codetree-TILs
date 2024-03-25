from sys import maxsize

# 사다리 타기 결과를 반환하는 함수
def get_result(l, x, y):
    result = [0 for _ in range(x)]
    for i in range(x):
        cur = i
        for j in range(y):
            if l[j][cur] == None:
                continue
            cur = l[j][cur]
        result[cur] = i

    return result

# 사다리를 추가해보면서 같은 결과가 나오는 최소 사다리 수를 구한다.
def get_min_bar(b, idx, l, x, y, fr, cnt):
    if idx == len(b): return maxsize

    min_cnt = maxsize
    # l에 bar를 추가한 경우와 아닌 경우로 나눠서 실행
    # bar를 추가하지 않은 경우
    if get_result(l, x, y) == fr:
        min_cnt = min(min_cnt, cnt)
    else:
        min_cnt = min(min_cnt, get_min_bar(b, idx + 1, l, x, y, fr, cnt))
    # bar를 추가한 경우
    c, r = b[idx]
    l[r][c], l[r][c + 1] = c + 1, c
    if get_result(l, x, y) == fr:
        min_cnt = min(min_cnt, cnt + 1)
    else:
        min_cnt = min(min_cnt, get_min_bar(b, idx + 1, l, x, y, fr, cnt + 1))
    l[r][c], l[r][c + 1] = None, None

    return min_cnt

n, m = [int(x) for x in input().split()]
bars = [[int(x) - 1 for x in input().split()] for _ in range(m)]

# 모든 사다리를 배치 후 결과 확인
max_y = 0
for i in range(m):
    max_y = max(max_y, bars[i][1])

ladder = [[None for _ in range(n)] for _ in range(max_y + 1)]
for x, y in bars:
    ladder[y][x], ladder[y][x + 1] = x + 1, x

first_result = get_result(ladder, n, max_y + 1)
print(get_min_bar(bars, 0, [[None for _ in range(n)] for _ in range(max_y + 1)], n, max_y + 1, first_result, 0))