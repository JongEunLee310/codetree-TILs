from sys import maxsize

# 재귀적으로 1번에서 다시 1번으로 돌아올 때까지 최소 비용을 구하는 함수
def min_cost(n, grid, r_visited, c_visited, cur_r, cnt, cost):
    if cnt == n: return sum(cost)
    
    min_c = maxsize
    for i in range(n):
        # 행과 열이 같은 위치는 선택할 수 없으므로 넘어간다
        if i == cur_r: continue
        # 1로 가는 선택은 가장 마지막에 해야하고 그 외에 cost가 0이 아닌 위치 중 방문하지 않은 행이나 열로 이동해야한다.
        if grid[cur_r][i] != 0 and (i == 0 and cnt + 1 == n or i != 0 and not r_visited[i] and not c_visited[i]):
            cost.append(grid[cur_r][i])
            r_visited[cur_r], c_visited[i] = True, True
            min_c = min(min_c, min_cost(n, grid, r_visited, c_visited, i, cnt + 1, cost))
            cost.pop()
            r_visited[cur_r], c_visited[i] = False, False

    return min_c

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]
r_visited, c_visited = [False for _ in range(n)], [False for _ in range(n)]
print(min_cost(n, grid, r_visited, c_visited, 0, 0, []))