import sys
from collections import deque

m,n,h = map(int,sys.stdin.readline().split())

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
data = [[list(map(int,sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

def bfs_3():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if -1 < nx < n and -1 < ny < m and -1 < nz < h:
                if data[nz][nx][ny] == 0:
                    data[nz][nx][ny] = data[z][x][y] + 1
                    queue.append((nz, nx, ny))

# 익은 토마토를 전부 queue에 삽입
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 1:
                queue.append((i,j,k))

bfs_3() # 익을 수 있는 토마토 전부 체크 완료(by 익게 된 날짜+1)
issuccess = 0
result = -2
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 0:
                issuccess = 1 # 끝까지 익지 못한 토마토가 있음
            result = max(result, data[i][j][k])

if issuccess == 1:
    print(-1)
elif result == -1: # 전부 비어있으면 0
    print(0)
else:
    print(result-1)
    # 전부 비었거나 & 익었거나 -> 1-1 = 0
    # 그냥 잘 익었으면 result-1