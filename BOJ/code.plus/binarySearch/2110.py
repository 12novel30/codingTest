import sys

n, c = map(int, sys.stdin.readline().split())
home = []
for i in range(n):
    home.append(int(sys.stdin.readline()))
home.sort()

start = sys.maxsize
for i in range(1,n):
    start = min(start, home[i]-home[i-1])
end = home[-1] - home[0]

while start <= end:
    mid = (start + end) // 2
    
    count = 1
    startHome = home[0]
    for i in range(1,n):
        if home[i]-startHome >= mid:
            count += 1
            startHome = home[i]
    
    if count >= c:
        start = mid + 1
    elif count < c:
        end = mid - 1
        
print(end)

'''
2. 이진 탐색 while문 조건: mid를 제한 길이로 설정했을 때, 블루레이의 개수가 m인가?
    1. count 계산: mid를 넘지 않으면 num 증가, 넘는 순간에 count 증가
    2. mid 변경: 정답 = **최소**이므로 counqwt **<** m에 =을 붙인다.
/*-----------------------------------------------------------------------------*/

mid = 최소 거리 중 최대
가장 인접한 두 공유기 사이의 최소 거리 기준
start = 1
end = 8
mid = 4
1 2 4 8 9
1, 8 - count=2



'''