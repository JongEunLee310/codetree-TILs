# 재귀적으로 행과 열이 겹치지 않도록 선택된 수의 최소값 중 최대값을 찾는 함수
def max_of_min(n, grid, c_visited, cur_r, l):
    if cur_r == n: return min(l)

    max_v = 0
    for i in range(n):
        if not c_visited[i]:
            l.append(grid[cur_r][i])
            c_visited[i] = True
            max_v = max(max_v, max_of_min(n, grid, c_visited, cur_r + 1, l))
            l.pop()
            c_visited[i] = False
    
    return max_v

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]
c_visited = [False for _ in range(n)]
print(max_of_min(n, grid, c_visited, 0, []))