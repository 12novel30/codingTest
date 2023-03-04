def solution(n, computers): # dfs
    node = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1:
                node[i].append(j)
    visited = [0]*n
    def dfs(v):
        visited[v] = 1
        for i in node[v]:
            if not visited[i]:
                dfs(i)
    answer = 0
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    
    return answer