# 재귀적으로 행과 열이 겹치지 않도록 선택한 값의 합 중 최대값을 구하는 함수
def max_sum(n, grid, c_visited, cnt, l):
    if cnt == n: return sum(l)

    max_s = 0
    for i in range(n):
        if not c_visited[i]:
            l.append(grid[cnt][i])
            c_visited[i] = True
            max_s = max(max_s, max_sum(n, grid, c_visited, cnt + 1, l))
            l.pop()
            c_visited[i] = False
    
    return max_s

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]
c_visited = [False for _ in range(n)]
print(max_sum(n, grid, c_visited, 0, []))