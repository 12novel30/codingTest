com = int(input())
connect = int(input())

visited = [False] * (com+1)

graph = [[]*com for _ in range(com+1)]
for i in range(connect):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
            
def dfs(s):
    global count 
    visited[s] = True

    for i in graph[s]:
        if not visited[i]:
            dfs(i)
            count += 1

dfs(1)

print(count)