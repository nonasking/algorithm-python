# DFS 기본 예시
# 각 노드가 연결된 정보를 표현한 2차원 리스트(예시)
graph = [
	[],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]
# 각 노드가 방문되었는지 여부를 표현한 1차원 리스트
visited = [False] * 9

# dfs 함수
def dfs(graph, v, visited):
	visited[v] = True
    for i in graph[v]:
    	if not visited[i]:
        	dfs(graph, i, visited)
            
# dfs 함수 호출(graph의 첫 번째 노드부터 깊이 우선하여 모두 탐색)
dfs(graph, 1, visited)