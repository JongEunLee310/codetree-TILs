# 모든 선분을 겹치지 않고 수직선 상에 올리는 모든 경우의 수 중 최대 선분 개수를 탐색
def max_lines(lines, n, idx, l):
    if idx == len(lines): return n

    max_n = n
    if not is_overlap(lines, l, idx):
        l.append(idx)
        max_n = max(max_n, max_lines(lines, n + 1, idx + 1, l))
        l.pop()
    max_n = max(max_n, max_lines(lines, n, idx + 1, l))

    return max_n

# 추가하려는 선분이 겹치는 여부를 판별하는 함수
def is_overlap(lines, l, i):
    result = False
    for idx in l:
        s, e = lines[idx]
        if in_range(lines[i][0], lines[i][1], s, e):
            result = True
            break
    return result

def in_range(x, y, s, e):
    return s <= x <= e or s <= y <= e or x <= s <= y or x <= e <= y

n = int(input())
lines = [[int(x) - 1 for x in input().split()] for _ in range(n)]
print(max_lines(lines, 0, 0, []))