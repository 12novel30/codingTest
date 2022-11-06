'''실전 2 위에서 아래로

## time = 2m/15m

## info
1. 입력받은 수를 내림차순으로 정렬

## Logic
- 파이썬 기본 라이브러리 사용
'''
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in array:
    print(i, end=' ')