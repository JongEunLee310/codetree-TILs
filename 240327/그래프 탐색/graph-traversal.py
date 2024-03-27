# graph 초기화하는 함수
def init_graph(n, v):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for n1, n2 in v:
        graph[n1][n2], graph[n2][n1] = 1, 1

# dfs로 1번 노드에서 도달 가능한 노드를 인접 행렬에 표시
def dfs(v, g, visited):
    pass


n, m = [int(x) for x in input().split()]
vertex = [[int(x) - 1 for x in input().split()] for _ in range(m)]
graph = init_graph(n, vertex) 

for i in range(n):
    print(graph[i])

visited = [False for i in range(n)]
dfs(vertex, graph, visited)