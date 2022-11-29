import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    name, korean, english, math = sys.stdin.readline().split()
    korean, english, math = int(korean), int(english), int(math)
    data.append([name, korean, english, math])

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
        # 국어 점수가 감소하는 순서로
        if left[left_id][1] < right[right_id][1]:
            merge_list.append(right[right_id])
            right_id += 1
        elif left[left_id][1] > right[right_id][1]:
            merge_list.append(left[left_id])
            left_id += 1
        else:
            # 영어 점수가 증가하는 순서로
            if left[left_id][2] > right[right_id][2]:
                merge_list.append(right[right_id])
                right_id += 1
            elif left[left_id][2] < right[right_id][2]:
                merge_list.append(left[left_id])
                left_id += 1
            else:
                # 수학 점수가 감소하는 순서로
                if left[left_id][3] < right[right_id][3]:
                    merge_list.append(right[right_id])
                    right_id += 1
                elif left[left_id][3] > right[right_id][3]:
                    merge_list.append(left[left_id])
                    left_id += 1
                else:
                    # 이름이 증가하는 순서로
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
    print(i[0])