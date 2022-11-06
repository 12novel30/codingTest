'''실전 3 떡볶이 떡 만들기
'''

''' 테스트케이스는 맞았는데 왕 별로인 내 풀이 ...
n,m = map(int, input().split())
first = list(map(int, input().split()))

second = []
tmp = 0
for i in range(n):
    for j in range(n):
        if first[i]<first[j]:
            tmp += first[j] - first[i]
    second.append(tmp)
    tmp = 0

third = sorted(second)

for i in range(n-1):
    if m == third[i]:
        index = second.index(m)
        answer = first[index]
    if third[i] < m and m < third[i+1]:
        count = third.index(third[i])
        index = second.index(third[i])
        answer = first[index]
        i = 0
        while m >= third[i]+(count+1)*i:
            i += 1
        answer += i

print(answer)
'''


    

'''input
4 6
19 15 10 17
'''

