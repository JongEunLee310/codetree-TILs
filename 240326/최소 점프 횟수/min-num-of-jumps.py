from sys import maxsize

# n번째 위치에 도달하기 위한 최소 점프 횟수를 구하는 함수
def min_jump(cur, cnt, n, j):
    if cur == n: return cnt
    if cur > n: return maxsize

    min_cnt = maxsize
    for i in range(1, j[cur] + 1):
        min_cnt = min(min_cnt, min_jump(cur + i, cnt + 1, n, j))
    
    return min_cnt

n = int(input()) - 1
jump = [int(x) for x in input().split()]
result = min_jump(0, 0, n, jump)
print(result) if result < maxsize else print(-1)