r,g,b = map(int, input().split())
answer = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(str(i)+' '+str(j)+' '+str(k))
            answer +=1
print(answer)