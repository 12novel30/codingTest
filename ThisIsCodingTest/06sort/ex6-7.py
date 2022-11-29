# 파이썬 라이브러리

array1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print("sorted(array)")
print(sorted(array1))

array2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print("array.sort()")
array2.sort()
print(array2)

array_with_key = [('바나나',2), ('키위', 5), ('귤', 3)]
def settingFunc(data):
    return data[1] # ('키위', 5)
print("sorted(array_with_key, key=settingFunc)")
print(settingFunc(array_with_key))
print(sorted(array_with_key, key=settingFunc))

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array = sorted(array)

array.sort()
array.sort(reverse=True)

array = sorted(array, key=lambda array:array[1])

array_with_key = [('바나나',2), ('키위', 5), ('귤', 3)]
def settingFunc(data):
    return data[1] # ('키위', 5)
print(settingFunc(array_with_key))
print(sorted(array_with_key, key=settingFunc))
