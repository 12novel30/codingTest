import sys

all = 0
dict = {}
while 1:
    word = sys.stdin.readline().rstrip()
    if word == '': break
    all += 1
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1
dict = sorted(dict.items())

for d in dict:
    # round는 쓰지 말자
    # print(d[0] + " " + str(round(d[1]/all*100, 4)))
    tmp = d[1]/all*100
    print("%s %.4f" %(d[0], tmp))