n = int(input())
num_list = list(map(int, input().split()))

answer = ''
for i in range(len(num_list)-1, -1, -1):
    answer += str(num_list[i]) + ' '
print(answer)