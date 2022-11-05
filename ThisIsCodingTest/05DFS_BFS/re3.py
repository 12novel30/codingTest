'''실전 3 음료수 얼려 먹기

## time = 55m/30m ++ 완전 틀림

## info
1. 구멍 뚫려있으면 0, 막히면 1
2. 연결되어있으면 아이스크림 완성
3. 리턴: 아이스크림 몇개?

## Logic
- dfs
1. 방문 여부 & 인접 노드는 모두 pan으로 설정
    - 방문) 0: false, 1: true
    - 인접) NWSE로 이동할 수 있는 칸
2. pan의 모든 칸에 대해
    - assert) pan을 벗어나면 패스
    - 1인(방문했다 치는 / 어차피 연결 안된) 칸은 패스
    - 0인(방문 아직 안한 / 연결안됐는데 연결할) 칸에 대해 **dfs 선회**
        - 현재 위치를 1(방문함)로 변경
        - 인접한 노드(NWSE)에 대해서 dfs 재귀 실행
        - return **true**
        - => 갈 수 있는 모든 칸을 1로 변경하고 최종 return true
    - return **true** = 연결되지 않았던 0으로 시작 & 연결된 애들을 전부 1로 변경 => **count ++**
'''

''' 내 삽질 답안 .. 이렇게 할 필요 없음
from collections import deque
def bfs_ics(s, pan, visited):
    queue = deque([s])
    visited[s[0]][s[1]] = True
    step = [(0,1),(-1,0),(0,-1),(1,0)]
    
    while queue:
        visit = queue.popleft()
        
        # 인접한 노드 리스트 만드는 과정
        for act in step:    
            nx = visit[0]+act[0]
            ny = visit[1]+act[1]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                
                # 인접노드 "중 0인 경우"를 전부 삽입 & 방문 처리
                if not visited[nx][ny]:
                    if pan[nx][ny] == 0:
                        queue.append((nx,ny))
                    visited[nx][ny] = True

n,m = map(int, input().split())
iceCount = 0
pan = []
for i in range(n):
    pan.append(list(map(int, input())))
visited = [[False for _ in range(m)] for __ in range(n)]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if pan[i][j] == 1:
                visited[i][j] = True
                continue
            bfs_ics((i,j), pan, visited)
            iceCount += 1

print(iceCount)
'''

from collections import deque

n,m = map(int, input().split())
pan = []
for i in range(n):
    pan.append(list(map(int, input())))
iceCount = 0

def dfs_ice(x,y):
    # 범위 벗어나면 즉시 종료
    if x < 0 and x >= n and y < 0 and y >= m:
        return False
    
    if pan[x][y] == 0:
        pan[x][y] = 1 # 현재 노드 방문 처리
        # 이동할 수 있는 부분을 재귀적으로 처리
        dfs_ice(x-1, y) # N
        dfs_ice(x, y-1) # W
        dfs_ice(x+1, y) # S
        dfs_ice(x, y+1) # E
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs_ice(i,j):
            iceCount += 1

print(iceCount)

'''input
4 5
00110
00011
11111
00000
'''