'''실전 2 왕실의 나이트

## time = 12m/20m

## info
1. c: abcdef...
2. r: 12345...
3. 나이트의 이동 방법:
    - (c+=2 or c-=2) and (r+=1 and r-=1) -> max 4가지
    - (r+=2 or r-=2) and (c+=1 and c-=1) -> max 4가지
4. 체스판: 8x8
5. 체스판 밖으로는 나갈 수 없다
6. 구하고자 하는 것: 나이트가 1번 움직일 수 있는 방법

## Logic
1. 내 풀이
    1. 각 경우별로 밖으로 나가는지 체크
2. 정답
    1. 각 액션을 리스트에 넣고 순회
'''

start = input()
# a: 97 h: 104
c = ord(start[0])
r = int(start[1])
count = 0

if c+2 >= 97 and c+2 <= 104:
    if r+1 >= 1 and r+1 <= 8:
        count+=1
    if r-1 >= 1 and r-1 <= 8:
        count+=1

if c-2 >= 97 and c-2 <= 104:
    if r+1 >= 1 and r+1 <= 8:
        count+=1
    if r-1 >= 1 and r-1 <= 8:
        count+=1

if r+2 >= 1 and r+2 <= 8:
    if c+1 >= 97 and c+1 <= 104:
        count+=1
    if c-1 >= 97 and c-1 <= 104:
        count+=1

if r-2 >= 1 and r-2 <= 8:
    if c+1 >= 97 and c+1 <= 104:
        count+=1
    if c-1 >= 97 and c-1 <= 104:
        count+=1

print(count)