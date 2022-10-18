n = int(input())
num_list = list(map(int, input().split()))

call_list = [0 for i in range(24)]
for i in num_list:
    call_list[i] += 1
print(' '.join(str(e) for e in call_list[1:]))