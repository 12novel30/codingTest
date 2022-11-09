''' 내 시간초과한 풀이 - 35m
n = int(input())
data = []
for i in range(n):
    start, end = map(int, input().split())
    data.append((start, end))
data = sorted(data, key = lambda x : (x[0], x[1]))

max_count = 0
first_end = data[0][1]
for i in range(n):
    
    if first_end < data[i][0]: break
    tmp_count = 1
    j = i
    k = 0
    
    while j+k < n:
        start = data[j][0]
        end = data[j][1]
        
        if end <= data[j+k][0]:
            tmp_count += 1
            j, k = j+k, 0
        else: k += 1
    
    if tmp_count >= max_count:
        max_count = tmp_count
        first_end = data[i][1]

print(max_count)
'''

n = int(input())
data = []
for i in range(n):
    start, end = map(int, input().split())
    data.append((start, end))
data = sorted(data, key = lambda x : (x[1], x[0]))

count = 1
end = data[0][1]
for i in range(1, n):
    if end <= data[i][0]:
        end = data[i][1]
        count += 1

print(count)