'''22-09-06 tue
[실전문제] 숫자 카드 게임 <fin>

3 3 
3 1 2
4 1 4 
2 2 2 
'''

N, M = map(int, input().split())
answer = 0

for i in range(N):
    data = list(map(int, input().split()))
    if answer < min(data):
        answer = min(data)

print(answer)