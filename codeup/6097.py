h, w = map(int, input().split())
board = [[0 for i in range(w)] for j in range(h)]
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d==1:
        for j in range(l):
            tmpx = x-1+j
            board[tmpx][y-1] = 1
    if d==0:
        for k in range(l):
            tmpy = y-1+k
            board[x-1][tmpy] = 1

for i in range(h):
    print(' '.join(str(e) for e in board[i]))