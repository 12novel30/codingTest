'''
1 2 3 4


이거 범위를 0 ~ 제일 작은 길이로 잡고
이진 탐색으로 각각 계산해서 줄여나가는게 베스트인듯!!
'''



import sys

k, n = map(int, sys.stdin.readline().split())
oh = [int(sys.stdin.readline()) for _ in range(k)]

start = 1
end = max(oh)
answer = start

while start <= end:
    mid = (start + end) // 2
    
    num = 0
    for d in oh:
        num += d//mid
    
    if num >= n:
        start = mid + 1
        answer = max(mid, answer)
    elif num < n:
        end = mid - 1
        
print(answer)