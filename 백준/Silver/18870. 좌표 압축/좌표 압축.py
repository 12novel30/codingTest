# 코테 준비중
n = int(input())
xlist = list(map(int, input().split()))
for i,x in enumerate(xlist):
    xlist[i] = [x,i]
xlist.sort()

answer = []
i = 0
count = 0
while i < len(xlist)-1:
    hold = i
    while xlist[i][0] == xlist[i+1][0]:
        i += 1
        if i == len(xlist)-1: break
    if hold == i: answer.append([count, xlist[i][1]])
    else:
        for _ in range(hold, i+1):
            answer.append([count, xlist[_][1]])
    i += 1
    count += 1

if len(answer) != len(xlist):
    answer.append([count, xlist[-1][1]])
    
answer = sorted(answer, key=lambda x: x[1])
for a in answer:
    print(a[0], end = ' ')