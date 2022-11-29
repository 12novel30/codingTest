from collections import deque

n = int(input())
start, end = map(int, input().split())
m = int(input())

visitedBFS = [0] * (n+1)

graph = [[]*n for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s): 
    queue = deque([s])
    
    while queue: # 빌 때까지 출력
        visit = queue.popleft()
        
        for i in graph[visit]:
            if visitedBFS[i]==0:
                queue.append(i)
                visitedBFS[i] = visitedBFS[visit] + 1 # 인접노드를 전부 삽입 & 방문 처리
    
    return visitedBFS[end]

visitedBFS[start]
answer = bfs(start)
if answer == 0:
    print(-1)
else:
    print(answer)