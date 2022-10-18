n = int(input())
checkerboard = [[0 for i in range(19)] for j in range(19)]

for i in range(n):
    x,y = map(int,input().split())
    checkerboard[x-1][y-1] = 1
for i in range(19):
    print(' '.join(str(e) for e in checkerboard[i]))
