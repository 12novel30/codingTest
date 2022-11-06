'''실전 2 부품 찾기
## time = 7m/30m
- 이진 탐색 전에는 무조건 정렬 진행 !!!!!! 안해서 큰일날뻔했다

## info
1. 5 가 있으면 yes, 없으면 no

## Logic
- 손님이 요청한 리스트의 번호가
- 창고 리스트 안에 있는지 확인
1. binary search를 m번 하든
2. 리스트 자체를 돌리든?
'''
n = int(input())
already_hand = list(map(int, input().split()))
already_hand.sort() ###### 이진 탐색 전에는 무조건 정렬 진행 !!!!!!
m = int(input())
request_hand = list(map(int, input().split()))

answer = ['no']*m

def bin_search(hand, target, start, end):
    if start > end:
        return None
    
    mid = (start+end)//2
    if hand[mid] == target:
        return mid
    elif target < hand[mid]:
        return bin_search(hand, target, start, mid-1)
    else:
        return bin_search(hand, target, mid+1, end)

## 여기는 내 답안
for i in range(len(request_hand)):
    if bin_search(already_hand, request_hand[i], 0, n-1) != None:
        answer[i] = 'yes'

for ans in answer:
    print(ans, end=' ')

## 이건 답지
for i in range(len(request_hand)):
    if bin_search(already_hand, request_hand[i], 0, n-1) != None:
        print('yes', end=' ')
    else: print('no', end=' ')

'''input
5
8 3 7 9 2
3
5 7 9

output
no yes yes
'''

## count sort 이용한 답지 ver2.
countSort = [0] * 1000001 # 1,000,001
for i in already_hand:
    countSort[i] = 1
for i in request_hand:
    if countSort[i] == 1:
        print('yes', end=' ')
    else: print('no', end=' ')

## set 이용한 ver3. -> 제일 간결함
already_hand = set(map(int, input().split()))
for i in already_hand:
    if i in request_hand:
        print('yes', end=' ')
    else: print('no', end=' ')