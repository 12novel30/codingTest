# quick sort - regular ver.
# 흠 이거 왜 안되지?

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_regular(array, start, end):
    
    if start >= end:
        return
    
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
    
    # center = right
    quick_sort_regular(array, start, right-1) # center 기준 왼편
    quick_sort_regular(array, right+1, end) # center 기준 오른편

quick_sort_regular(array, 0, len(array)-1)
print(array)