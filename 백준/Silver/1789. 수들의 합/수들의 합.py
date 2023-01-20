import sys

s = int(sys.stdin.readline())
tmp = int((s*2)**(1/2))
while True:
    if tmp*(tmp+1) <= s*2 and s*2 <= (tmp+1)*(tmp+2):
        print(tmp)
        break
    else:
        tmp -= 1