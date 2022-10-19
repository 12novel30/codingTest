box = []
xhere = 1
yhere = 1
for i in range(10):
    box.append(list(map(int, input().split())))

box[yhere][xhere] = 9
while True:
    if box[yhere][xhere+1] != 1: xhere += 1
    else:
        if box[yhere+1][xhere] != 1: yhere += 1
        else: break
    
    if box[yhere][xhere] == 2:
        box[yhere][xhere] = 9
        break
    else: box[yhere][xhere] = 9

for i in range(10):
    print(' '.join(str(e) for e in box[i]))