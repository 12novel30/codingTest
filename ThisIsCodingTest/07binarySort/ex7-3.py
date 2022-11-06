# 이진 탐색 - iterative ver.

n, target = map(int, input().split())
hand = list(map(int, input().split()))

def binarySearch_iterative(hand, target, start, end):
    
    while start <= end:
        mid = (start+end)//2

        if hand[mid] == target:
            return mid
        elif target < hand[mid]:
            end = mid-1
        else:
            start = mid+1
    return None

sound = binarySearch_iterative(hand, target, 0, n-1)
if sound == None:
    print("원소 없음")
else:
    print(sound+1)