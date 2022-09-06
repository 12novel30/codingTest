'''22-09-06 tue
[실전문제] 숫자 카드 게임 <fin>

3 3 
3 1 2
4 1 4 
2 2 2 
'''

n, m = map(int, input().split())
# answer ... 답 보지 말기
maxi = 0
for i in range(n):
    data = list(map(int, input().split()))
    if min(data)>maxi:
        maxi = min(data)
print(maxi)