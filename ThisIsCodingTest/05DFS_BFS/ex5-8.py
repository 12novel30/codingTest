''' DFS
## logic
1. 방문 여부를 확인할 리스트 visited 준비
2. 인접한 노드가 있는 리스트 graph 준비
3. graph를 **dfs로 선회**
    - 현재 위치를 visited = true로 변경
    - 인접한 노드에 대해서 **dfs 재귀** 실행
'''
def dfs(graph, s, visited): 
    visited[s] = True
    print(s, end=' ')
    
    for i in graph[s]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False]*9 # 0~8
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

dfs(graph, 1, visited)