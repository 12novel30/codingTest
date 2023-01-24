import sys

n = int(sys.stdin.readline())
game = []
maxMap = [0,0,0]
minMap = [0,0,0]

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    if i == 0:
        maxMap[0], maxMap[1], maxMap[2] = a, b, c
        minMap[0], minMap[1], minMap[2] = a, b, c
    else:
        tmpA = max(maxMap[0], maxMap[1]) + a
        tmpB = max(maxMap) + b
        tmpC = max(maxMap[1], maxMap[2]) + c
        maxMap[0], maxMap[1], maxMap[2] = tmpA, tmpB, tmpC
        
        tmpA = min(minMap[0], minMap[1]) + a
        tmpB = min(minMap) + b
        tmpC = min(minMap[1], minMap[2]) + c
        minMap[0], minMap[1], minMap[2] = tmpA, tmpB, tmpC
        
print(str(max(maxMap)) + " " + str(min(minMap)))
