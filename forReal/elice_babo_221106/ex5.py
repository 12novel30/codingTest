array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
#30
def solution(kyul):
    count = 0
    for i in range(len(kyul)-1):
        if kyul[i] > kyul[i+1]:
            count += 1
    return count

# 테케도 틀림 ㅋㅋ
def solution(kyul):
    count = 0
    for i in range(len(kyul)-1):
        for j in range(i+1, len(kyul)):
            if kyul[i] < kyul[j]:
                break
            else:
                count += 1
    return count


def solution(kyul):
    return quick_sort(kyul, 0, len(kyul)-1, 0)

def quick_sort(array, start, end, swapping):
    if start >= end:
        return 0
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while start < right and array[pivot] <= array[right]:
            right -= 1
            
        if left > right: # 엇갈렸다면
            # pivot보다 처음 작기 시작한 right <-> pivot
            array[pivot], array[right] = array[right], array[pivot]
        else: # 엇갈리지 않았다면
            # 작은 애들 중 가장 큰 값 <-> 큰 애들 중 가장 작은 값
            array[left], array[right] = array[left], array[right]
        swapping += 1
    
    # center = right
    swapping += quick_sort(array, start, right-1, swapping) # center 기준 왼편
    swapping += quick_sort(array, right+1, end, swapping) # center 기준 오른편
    
    return swapping