# 이진 탐색 - recursive ver

n, target = map(int, input().split())
hand = list(map(int, input().split()))

def binarySearch_recursive(hand, target, start, end):
    
    if start>end: return None
    
    mid = (start+end)//2
    if hand[mid] == target:
        return mid
    elif target < hand[mid]:
        return binarySearch_recursive(hand, target, start, mid-1)
    else:
        return binarySearch_recursive(hand, target, mid+1, end)

sound = binarySearch_recursive(hand, target, 0, n-1)
if sound == None:
    print("원소 없음")
else:
    print(sound+1)