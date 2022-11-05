'''실전 4 미로 탈출

## time = over/30m
- re3보다는 잘 풀었는데, 좀 더 연습하면 될 것 같다
- 경로수를 체크할 때는 이전 값 + 1 ... 메모

## info
1. 현 위치는 1,1 = 0,0
2. 출구는 n,m = n-1,m-1
3. 0(괴물)은 피해야하고
4. 1은 이동 가능 -> n-1, m-1까지 가야한다
5. 최소 경로의 길이 print

## Logic
- bfs
- 이동 경로 수: 이동하면서 각 칸에 표시
1. 방문 여부 & 인접 모두 maze로
    - 방문: 1->0
    - 인접: 상 하 좌 우 의 0인 모든 칸
        - maze를 벗어나면 패스
        - 괴물(1)이면 패스
2. maze의 0,0부터 모든 칸을 **bfs로 선회**
    - 현재 위치를 queue에 넣기
    - 현재 위치는 변경 x !!! -> 맨 처음은 0이 맞고, 이동하면 +1이기 때문.
    - 연결되어 있는 노드 중 non pass인 경우
        - queue.append
        - maze[nx][ny] = maze[x][y] + 1; 이전의 값에서 1을 증가시킨다
        - => 경로를 한 칸 증가시켰음을 의미
'''

''' 내 망한 코드
from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))
queue = deque()
step = [(-1,0), (0,-1), (1,0), (0,1)]

def bfs_maze(x,y, count):
    queue.append((x,y))
    maze[x][y] = 0
    
    while queue:
        now = queue.popleft()
        count += 1
        appendCount = False
        nx = now[0]
        ny = now[1]
        for act in step:
            nnx = x + act[0]
            nny = y + act[1]
            if nnx >= 0 and nnx < n and nny >= 0 and nny < m:
                if maze[nnx][nny] == 1:
                    appendCount = True
                    if nnx == n-1 and nny == m-1:
                        break
                    queue.append((nnx,nny))
                    maze[nnx][nny] = 0

        if not appendCount: count -= 1
    return count

count = bfs_maze(0,0,0)
print(count)
'''

from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))
queue = deque()
step = [(-1,0), (1,0), (0,-1), (0,1)] # 상 하 좌 우

# 지나온 길에 몇번째 이동인지 적기
def bfs_maze(x,y):
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        for act in step:
            nx = x + act[0]
            ny = y + act[1]
            
            # 벗어나면 패스
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            # 벽이면 패스
            if [nx][ny] == 0: continue
            
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
    
    return maze[n-1][m-1]

print(bfs_maze(0,0))

'''input
5 6
101010
111111
000001
111111
111111
'''