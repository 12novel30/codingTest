import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

#Merge Sort
def merge_2(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = merge_2(array[:mid])
    right = merge_2(array[mid:])
    
    return merge_func_2(left, right)

def merge_func_2(left, right):
    merge_list = []
    left_id, right_id = 0, 0
    
    #case1 left, right
    while len(left) > left_id and len(right) > right_id:
        if left[left_id][1] > right[right_id][1]:
            merge_list.append(right[right_id])
            right_id += 1
        elif left[left_id][1] < right[right_id][1]:
            merge_list.append(left[left_id])
            left_id += 1
        else:
            if left[left_id][0] > right[right_id][0]:
                merge_list.append(right[right_id])
                right_id += 1
            else:
                merge_list.append(left[left_id])
                left_id += 1
    
    #case2 left
    while len(left) > left_id and len(right) <= right_id:
        merge_list.append(left[left_id])
        left_id += 1
    
    #case3 right
    while len(right) > right_id and len(left) <= left_id:
        merge_list.append(right[right_id])
        right_id += 1
    
    return merge_list

result = merge_2(data)
for i in result:
    print(str(i[0]) + " " + str(i[1]))