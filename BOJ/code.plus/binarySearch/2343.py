'''
최대한 균일하게 3등분 하는 것이 중요'''


import sys

n, m = map(int, sys.stdin.readline().split())
lecture = list(map(int, sys.stdin.readline().split()))

start = max(lecture)
end = sum(lecture)
answer = end

while start <= end:
    mid = (start + end) // 2
    
    count = 1
    num = 0
    for l in lecture:
        if num + l <= mid:
            num += l
        else:
            num = l # new bluelay
            count += 1
    
    if count > m:
        start = mid + 1
    elif count <= m: # 가능한 것들 중 작은 것을 리턴해야하므로 여기에 =을 붙임.
        end = mid - 1
        answer = min(mid, answer)
        
print(answer)