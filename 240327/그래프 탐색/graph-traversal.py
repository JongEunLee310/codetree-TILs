# graph 초기화하는 함수
def init_graph(n, v):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for n1, n2 in v:
        graph[n1][n2], graph[n2][n1] = 1, 1

    return graph

# dfs로 1번 노드에서 도달 가능한 노드를 인접 행렬에 표시
def dfs(vertex, g, visited, cur_n):
    for nxt_n in range(len(visited)):
        if graph[cur_n][nxt_n] == 1 and not visited[nxt_n]:
            visited[nxt_n] = True
            dfs(vertex, g, visited, nxt_n)


n, m = [int(x) for x in input().split()]
vertex = [[int(x) - 1 for x in input().split()] for _ in range(m)]
graph = init_graph(n, vertex) 

visited = [False for i in range(n)]
visited[0] = True
dfs(vertex, graph, visited, 0)

# 방문한 노드의 개수를 카운트
cnt = 0
for i in range(1, len(visited)):
    if visited[i]: cnt += 1
print(cnt)