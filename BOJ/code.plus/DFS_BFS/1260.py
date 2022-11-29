from collections import deque

n,m,v = map(int, input().split())

visitedDFS = [False] * (n+1)
visitedBFS = [False] * (n+1)

def insertList(list, a):
    if len(list) == 0:
        return [a]
    if a <= list[0]:
        return [a]+list
    else:
        for i in range(len(list)):
            if a<=list[i]:
                return list[:i]+[a]+list[i:]
        return list+[a]

graph = [[]*n for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a] = insertList(graph[a], b)
    graph[b] = insertList(graph[b], a)

def dfs(s):
    visitedDFS[s] = True
    print(s, end=' ')

    for i in graph[s]:
        if not visitedDFS[i]:
            dfs(i)

def bfs(s): 
    queue = deque([s])
    visitedBFS[s] = True
    
    while queue: # 빌 때까지 출력
        visit = queue.popleft()
        print(visit, end=' ')
        
        for i in graph[visit]:
            if not visitedBFS[i]:
                queue.append(i)
                visitedBFS[i] = True # 인접노드를 전부 삽입 & 방문 처리

dfs(v)
print()
bfs(v)