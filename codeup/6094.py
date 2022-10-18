n = int(input())
num_list = list(map(int, input().split()))

first = num_list[0]
for i in num_list:
    if first > i: first = i
print(first)