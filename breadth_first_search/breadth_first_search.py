# BFS 기본 예시
def bfs(graph, start, visited):
	queue = deque([start])
    visited(start) = True
    
    while queue:
    	v = queue.popleft()
        for i in graph[v]:
        	if not visited[i]:
            	queue.append(i)
                visited[i] = True
            
# dfs 함수 호출(graph의 첫 번째 노드부터 깊이 우선하여 모두 탐색)
bfs(graph, 1, visited)