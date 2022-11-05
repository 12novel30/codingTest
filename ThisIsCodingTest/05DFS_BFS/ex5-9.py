''' BFS
## logic
1. 방문 여부를 확인할 리스트 visited 준비
2. 인접한 노드가 있는 리스트 graph 준비
3. graph를 **bfs로 선회**
    - 현재 위치를 queue에 넣기
    - 현재 위치를 visited = true로 변경
    - 인접한 노드 중 visited = false인 경우
        - queue.append
        - visited = true
'''
from collections import deque
def bfs(graph, s, visited): 
    queue = deque([s])
    visited[s] = True
    
    while queue: # 빌 때까지 출력
        visit = queue.popleft()
        print(visit, end=' ')
        
        for i in graph[visit]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True # 인접노드를 전부 삽입 & 방문 처리
    

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

bfs(graph, 1, visited)