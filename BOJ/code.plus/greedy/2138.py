'''
0
1
-> 1번

00
11 -> 1번


'''


n = int(input())
nowState = list(map(int, input()))
goalState = list(map(int, input()))
count = 0
count32 = 0
count23 = 0

def change3(i):
    nowState[i] = 1 - nowState[i]
    nowState[i+1] = 1 - nowState[i+1]
    nowState[i+2] = 1 - nowState[i+2]
    print(nowState)

def change2(i):
    nowState[i] = 1 - nowState[i]
    nowState[i+1] = 1 - nowState[i+1]
    print(nowState)

if n == 1 or n == 2:
    if nowState != goalState:
        change2(0)
        count += 1
if n >= 3:
    if nowState[0:2] != goalState[0:2]:
        change2(0)
        count += 1
    if nowState != goalState:        
        for i in range(0, n-2):
            if nowState[i] != goalState[i]:
                change3(i)
                count += 1
            if nowState == goalState:
                break
        
        if nowState[-1] != goalState[-1]:
            change2(-2)
            count += 1

if nowState == goalState:
    print(count)
else:
    print(-1)