n = int(input())
xlist = list(map(int, input().split()))
xset = sorted(set(xlist))
dict = {xset[i] : i for i in range(len(xset))}
for d in xlist:
    print(dict[d], end = ' ')
