### 다시 풀어볼 것
3. 그리디;
4. 구현; re3
5. 깊이탐색; ex5-8, ex5-9, re3, re4
6. 정렬; ex6-5(퀵), ex6-6(계수)
7. 이진탐색; ex7-2(재귀)

### 3,4 
```
N, M, K = map(int, input().split())

data = list(map(int, input().split()))
data.sort(reverse=True)

action = input().split()

c = ord(start[0])

def turn_left(): # chap2-04-re3
    global nowDir
    nowDir -= 1
    if nowDir == -1:
        nowDir = 3
```

### 5
```
stack.pop()
print(stack) # 최하단부터
print(stack[::-1]) # 최상단부터

from collections import deque
queue = deque()
queue = deque([s])
queue.popleft()
print(queue) # 나중에 온 애들부터
queue.reverse()
print(queue) # 먼저 온 애들부터

DFS: ex5-8
BFS: ex5-9

tmp = list(map(int, input())) # integer input ex) 00000
```

### 7
```
import sys
data = sys.stdin.readline().rstrip()
```