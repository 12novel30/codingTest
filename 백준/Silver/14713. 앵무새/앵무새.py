# 코테 준비중
n = int(input())
pps = []
for _ in range(n):
    pps.append(input().split())

cse = input().split()
for c in cse:
    can = False
    for p in pps:
        if len(p) != 0 and p[0] == c:
            p.pop(0)
            can = True
            break
    if can == False: break

    
left = 0
for p in pps: left += len(p)
if can == True and left == 0:
    print("Possible")
else:
    print("Impossible")
            