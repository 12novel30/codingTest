# 코테 준비중
import heapq as hq
import sys

n = int(input())
h = []
for _ in range(n):
    i = int(sys.stdin.readline()) 
    if i == 0:
        if len(h) == 0:
            print(0)
        else:
            tmp = hq.heappop(h)
            print(tmp[1])
    else:
        hq.heappush(h, [abs(i), i])