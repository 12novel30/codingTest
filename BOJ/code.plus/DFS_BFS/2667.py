from collections import deque

n = int(input())

pan = []
for i in range(n):
    pan.append(list(map(int, input())))
iceCount = 0

def dfs_ice(x,y):
    # 범위 벗어나면 즉시 종료
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    
    if pan[x][y] == 1:
        pan[x][y] = 0 # 현재 노드 방문 처리
        # 이동할 수 있는 부분을 재귀적으로 처리
        return 1 + dfs_ice(x-1, y) + dfs_ice(x, y-1) + dfs_ice(x+1, y) + dfs_ice(x, y+1)
    return 0

answer = []
for i in range(n):
    for j in range(n):
        tmp = dfs_ice(i,j)
        if tmp != 0:
            iceCount += 1
            answer.append(tmp)
            
print(iceCount)
answer.sort()
for ans in answer:
    print(ans)