import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(tree)
answer = start

while start <= end:
    mid = (start + end) // 2
    
    num = 0
    for t in tree:
        if t >= mid:
            num += t-mid
        if num > m: ## 시간 초과 해결
            break
    
    if num >= m:
        start = mid + 1
        answer = max(mid, answer)
    elif num < m:
        end = mid - 1
    # else:
    #     break
        
print(answer)