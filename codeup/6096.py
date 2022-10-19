checkerboard = []
for i in range(19):
    checkerboard.append(list(map(int, input().split())))

n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    for p in range(19):
        if checkerboard[x-1][p] == 0: checkerboard[x-1][p] = 1
        else: checkerboard[x-1][p] = 0
        if checkerboard[p][y-1] == 0: checkerboard[p][y-1] = 1
        else: checkerboard[p][y-1] = 0

for i in range(19):
    print(' '.join(str(e) for e in checkerboard[i]))