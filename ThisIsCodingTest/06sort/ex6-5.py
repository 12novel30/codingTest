# quick sort - python ver.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_python(array):
    
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)
    
print(quick_sort_python(array))